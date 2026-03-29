#!/usr/bin/env python3
"""Generate a machine-readable audit for the bibliography."""

from __future__ import annotations

import argparse
import csv
import json
import re
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional
from urllib.parse import quote

import bibtexparser
import requests


DEFAULT_BIB = Path("latex/references.bib")
DEFAULT_JSON = Path("verification/verification.json")
DEFAULT_CSV = Path("verification/verification.csv")
COUNT_PATTERNS = {
    "README.md": re.compile(r"\|\s*\*\*Total references\*\*\s*\|\s*\*\*(\d+)\*\*"),
    "README-zh-TW.md": re.compile(r"\|\s*\*\*引用總數\*\*\s*\|\s*\*\*(\d+)\*\*"),
    "markdown/en/VERIFICATION-REPORT.md": re.compile(r"Total references:\s*\*\*(\d+)\*\*"),
    "markdown/zh-TW/VERIFICATION-REPORT-zh-TW.md": re.compile(
        r"(?:引用總數[:：]?\s*\*\*(\d+)\*\*|全部\s*(\d+)\s*篇參考文獻)"
    ),
}
USER_AGENT = (
    "CosmicDiasporaHypothesisVerification/0.1 "
    "(https://github.com/djchrisssssss/cosmic-diaspora-hypothesis)"
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Verify bibliography identifiers and export JSON/CSV audit files.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--bib", type=Path, default=DEFAULT_BIB, help="Path to the BibTeX file.")
    parser.add_argument(
        "--json-output",
        type=Path,
        default=DEFAULT_JSON,
        help="Machine-readable JSON output path.",
    )
    parser.add_argument(
        "--csv-output",
        type=Path,
        default=DEFAULT_CSV,
        help="Flat CSV output path.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=15.0,
        help="HTTP timeout in seconds for DOI and URL checks.",
    )
    parser.add_argument(
        "--sleep-seconds",
        type=float,
        default=0.1,
        help="Delay between online requests.",
    )
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Skip network checks and only validate identifier presence and document counts.",
    )
    return parser


def parse_reference_numbers(raw_bib: str) -> Dict[str, int]:
    pattern = re.compile(r"%\s*\[(\d+)\]\s*\n@\w+\{([^,]+),", re.MULTILINE)
    return {key.strip(): int(number) for number, key in pattern.findall(raw_bib)}


def load_entries(bib_path: Path) -> List[dict]:
    with bib_path.open("r", encoding="utf-8") as handle:
        parser = bibtexparser.bparser.BibTexParser(common_strings=True)
        parser.ignore_nonstandard_types = False
        database = bibtexparser.load(handle, parser=parser)
    return database.entries


def extract_url(entry: dict) -> Optional[str]:
    if entry.get("url"):
        return entry["url"].strip()

    howpublished = entry.get("howpublished", "")
    match = re.search(r"\\url\{([^}]+)\}", howpublished)
    if match:
        return match.group(1).strip()

    return None


def normalize_source(entry: dict) -> dict:
    doi = entry.get("doi", "").strip() or None
    url = extract_url(entry)
    eprint = entry.get("eprint", "").strip() or None
    archive_prefix = entry.get("archiveprefix", "").strip().lower()

    checked_url = None
    source_type = "manual"

    if doi:
        source_type = "doi"
        checked_url = f"https://api.crossref.org/works/{quote(doi)}"
    elif url:
        source_type = "url"
        checked_url = url
    elif eprint and archive_prefix == "arxiv":
        source_type = "arxiv"
        checked_url = f"https://arxiv.org/abs/{eprint}"

    return {
        "doi": doi,
        "url": url,
        "eprint": eprint,
        "archive_prefix": archive_prefix or None,
        "source_type": source_type,
        "checked_url": checked_url,
    }


def verify_doi(doi: str, checked_url: str, session: requests.Session, timeout: float) -> dict:
    try:
        response = session.get(checked_url, timeout=timeout)
        payload = response.json()
        message = payload.get("message", {})
        titles = message.get("title") or []
        return {
            "verification_status": "verified" if response.ok else "failed",
            "http_status": response.status_code,
            "resolved_url": message.get("URL"),
            "resolved_identifier": message.get("DOI"),
            "resolved_title": titles[0] if titles else None,
            "notes": None if response.ok else f"Crossref returned status {response.status_code}",
        }
    except (requests.RequestException, ValueError, KeyError) as exc:
        fallback_url = f"https://doi.org/{quote(doi)}"
        try:
            response = session.get(fallback_url, timeout=timeout, allow_redirects=True, stream=True)
            status_code = response.status_code
            if 200 <= status_code < 400:
                status = "verified"
                notes = f"Crossref fallback via doi.org after: {exc}"
            elif status_code in {401, 403}:
                status = "restricted"
                notes = f"doi.org resolved but endpoint returned {status_code} after Crossref fallback: {exc}"
            elif status_code == 429:
                status = "rate_limited"
                notes = f"doi.org rate-limited the request after Crossref fallback: {exc}"
            else:
                status = "failed"
                notes = f"Crossref fallback failed with doi.org status {status_code}: {exc}"

            result = {
                "verification_status": status,
                "http_status": status_code,
                "resolved_url": response.url,
                "resolved_identifier": doi,
                "resolved_title": None,
                "notes": notes,
            }
            response.close()
            return result
        except requests.RequestException as fallback_exc:
            return {
                "verification_status": "error",
                "http_status": None,
                "resolved_url": None,
                "resolved_identifier": doi,
                "resolved_title": None,
                "notes": f"Crossref error: {exc}; doi.org fallback error: {fallback_exc}",
            }


def verify_url(checked_url: str, session: requests.Session, timeout: float) -> dict:
    try:
        response = session.get(checked_url, timeout=timeout, allow_redirects=True, stream=True)
        status_code = response.status_code
        if 200 <= status_code < 400:
            status = "verified"
            notes = None
        elif status_code in {401, 403}:
            status = "restricted"
            notes = f"Endpoint responded with {status_code}; resource may be bot-protected."
        elif status_code == 429:
            status = "rate_limited"
            notes = "Endpoint rate-limited the request."
        else:
            status = "failed"
            notes = f"Endpoint responded with {status_code}."

        result = {
            "verification_status": status,
            "http_status": status_code,
            "resolved_url": response.url,
            "resolved_identifier": checked_url,
            "resolved_title": None,
            "notes": notes,
        }
        response.close()
        return result
    except requests.RequestException as exc:
        return {
            "verification_status": "error",
            "http_status": None,
            "resolved_url": None,
            "resolved_identifier": checked_url,
            "resolved_title": None,
            "notes": str(exc),
        }


def extract_declared_counts(repo_root: Path, parsed_total: int) -> List[dict]:
    results = []
    for relative_path, pattern in COUNT_PATTERNS.items():
        path = repo_root / relative_path
        declared_count = None
        matches_bib = False
        if path.exists():
            text = path.read_text(encoding="utf-8")
            match = pattern.search(text)
            if match:
                declared_count = next((int(group) for group in match.groups() if group), None)
                matches_bib = declared_count == parsed_total
        results.append(
            {
                "path": relative_path,
                "declared_count": declared_count,
                "matches_bib_count": matches_bib,
            }
        )
    return results


def verify_entries(
    entries: Iterable[dict],
    reference_numbers: Dict[str, int],
    session: requests.Session,
    timeout: float,
    sleep_seconds: float,
    offline: bool,
) -> List[dict]:
    verified = []
    sorted_entries = sorted(entries, key=lambda entry: reference_numbers.get(entry["ID"], 10**9))
    for entry in sorted_entries:
        normalized = normalize_source(entry)
        key = entry["ID"]
        result = {
            "reference_number": reference_numbers.get(key),
            "key": key,
            "entry_type": entry.get("ENTRYTYPE"),
            "title": entry.get("title"),
            "year": entry.get("year"),
            **normalized,
        }

        if offline:
            result.update(
                {
                    "verification_status": (
                        "identifier_present"
                        if normalized["source_type"] != "manual"
                        else "manual_review_required"
                    ),
                    "http_status": None,
                    "resolved_url": normalized["checked_url"],
                    "resolved_identifier": normalized["doi"]
                    or normalized["url"]
                    or normalized["eprint"],
                    "resolved_title": None,
                    "notes": "Network checks skipped (--offline).",
                }
            )
        elif normalized["source_type"] == "doi":
            result.update(verify_doi(normalized["doi"], normalized["checked_url"], session, timeout))
            time.sleep(sleep_seconds)
        elif normalized["source_type"] in {"url", "arxiv"}:
            result.update(verify_url(normalized["checked_url"], session, timeout))
            time.sleep(sleep_seconds)
        else:
            result.update(
                {
                    "verification_status": "manual_review_required",
                    "http_status": None,
                    "resolved_url": None,
                    "resolved_identifier": None,
                    "resolved_title": None,
                    "notes": "No DOI, URL, or arXiv identifier found.",
                }
            )

        verified.append(result)

    return verified


def build_summary(results: List[dict], declared_counts: List[dict], offline: bool) -> dict:
    source_counts = Counter(result["source_type"] for result in results)
    status_counts = Counter(result["verification_status"] for result in results)
    manual_keys = [result["key"] for result in results if result["verification_status"] == "manual_review_required"]

    return {
        "total_references": len(results),
        "offline": offline,
        "source_counts": dict(source_counts),
        "status_counts": dict(status_counts),
        "manual_review_keys": manual_keys,
        "document_count_consistency": {
            "all_matched": all(item["matches_bib_count"] for item in declared_counts if item["declared_count"] is not None),
            "checked_files": declared_counts,
        },
    }


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: List[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "reference_number",
        "key",
        "entry_type",
        "source_type",
        "verification_status",
        "title",
        "year",
        "doi",
        "url",
        "eprint",
        "archive_prefix",
        "checked_url",
        "resolved_url",
        "resolved_identifier",
        "resolved_title",
        "http_status",
        "notes",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field) for field in fieldnames})


def main() -> int:
    args = build_parser().parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    bib_path = (repo_root / args.bib).resolve() if not args.bib.is_absolute() else args.bib
    json_output = (repo_root / args.json_output).resolve() if not args.json_output.is_absolute() else args.json_output
    csv_output = (repo_root / args.csv_output).resolve() if not args.csv_output.is_absolute() else args.csv_output

    raw_bib = bib_path.read_text(encoding="utf-8")
    reference_numbers = parse_reference_numbers(raw_bib)
    entries = load_entries(bib_path)
    declared_counts = extract_declared_counts(repo_root, len(entries))

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    results = verify_entries(
        entries=entries,
        reference_numbers=reference_numbers,
        session=session,
        timeout=args.timeout,
        sleep_seconds=args.sleep_seconds,
        offline=args.offline,
    )

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "bib_path": str(bib_path.relative_to(repo_root)),
        "json_output": str(json_output.relative_to(repo_root)),
        "csv_output": str(csv_output.relative_to(repo_root)),
        "summary": build_summary(results, declared_counts, args.offline),
        "entries": results,
    }
    write_json(json_output, payload)
    write_csv(csv_output, results)

    print(
        json.dumps(
            {
                "json_output": str(json_output.relative_to(repo_root)),
                "csv_output": str(csv_output.relative_to(repo_root)),
                "summary": payload["summary"],
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
