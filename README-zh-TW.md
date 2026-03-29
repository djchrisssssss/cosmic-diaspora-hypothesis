**[English Version](./README.md)**

# 宇宙播遷假說

**Cosmic Diaspora Hypothesis**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18965614.svg)](https://doi.org/10.5281/zenodo.18965614)

一個結構化的假說框架，探討宇宙生命的統計基礎、文明演化的能量與材料門檻，以及外星現象的多來源分類模型——以物理學、工程可行性與可證偽推理為基礎。

> 這是一份持續更新的文件。歡迎貢獻、批判與證偽嘗試。

![宇宙播遷假說](./assets/cover.png)

---

## 作者

**Kris Lai**
- Email: kriss@scallop.io
- ORCID: [0009-0000-2223-4826](https://orcid.org/0009-0000-2223-4826)
- 機構: [Scallop Labs](https://www.scallop.io/)

---

## 文件

| 文件 | 語言 | 說明 |
|------|------|------|
| [`hypothesis-en.md`](./markdown/en/hypothesis-en.md) | English | 完整英文版假說架構（Markdown） |
| [`hypothesis-zh-TW.md`](./markdown/zh-TW/hypothesis-zh-TW.md) | 正體中文 | 完整正體中文版假說架構 |
| [`latex/main.tex`](./latex/main.tex) | English | 供 Overleaf 產出 PDF 的 LaTeX 排版來源 |
| [`VERIFICATION-REPORT.md`](./markdown/en/VERIFICATION-REPORT.md) | English | 科學驗證報告 |
| [`VERIFICATION-REPORT-zh-TW.md`](./markdown/zh-TW/VERIFICATION-REPORT-zh-TW.md) | 正體中文 | 科學驗證報告（中文版） |

---

## 驗證摘要

所有事實宣稱與引用文獻均已透過計算工具與公開資料庫進行獨立驗證。

| 類別 | 驗證結果 | 方法 |
|------|---------|------|
| 天文物理宣稱 | 13/13 | `astropy`（Planck18 宇宙學模型） |
| 生物學宣稱 | 7 | PubMed / NCBI 文獻回顧 |
| 物理與工程宣稱 | 13 | 同行評審文獻 |
| DOI 引用 | 37/37 | CrossRef REST API |
| 純 URL 引用 | 17 | 機構來源目錄 |
| 本次修訂新增引用 | 12 | [55]–[66]：費米消解、生命起源貝氏分析、NfoLD 框架、技術標記可偵測性、金星約束、3I/ATLAS、Rubin 天文台 |
| **引用總數** | **66** | |

> 完整方法論、逐項驗證表格及 DOI 審計結果詳見[驗證報告](./markdown/zh-TW/VERIFICATION-REPORT-zh-TW.md)。

---

## 架構總覽

- **0. 方法論與研究範圍** — 問題定義、可證偽性、觀測選擇效應（人擇原理）、認識論分層、統計宇宙學框架
- **第一部分：宇宙生命擴散基礎** — 恆星形成、宜居帶、極端生命、岩石轉移、生命起源機率約束（§1.6）
- **第二部分：文明演化與技術門檻** — 能源階層、核融合燃料循環約束、材料突破、材料系統整合限制（§3.3.4）、小型化核融合、超材料
- **第三部分：外星事件結構分類** — 當代外星事件的 7 種來源分類模型、SETI 定向通訊限制
- **第四部分：文明存在模型** — 貝氏先驗評估表、太陽系外觀測者、遠古火星文明、遠古金星文明（含 2024–2026 平衡文獻約束）、遠古地球文明、泛種論與定向播遷區分標準
- **第五部分：基地工程與隱蔽矩陣** — 選址、能源自給、電磁與熱特徵抑制、金星大氣能量收支與參數敏感度分析
- **第七部分：跨星系任務架構與人類定位** — 部署邏輯、文明重置週期、記憶壓縮、人類任務定位
- **第八部分：可驗證與觀測路徑** — 儀器門檻偵測表（§13.0）、地下成像、深海掃描、引力異常監測、星際天體光譜分析含 3I/ATLAS（§13.7）
- **附錄 A：認知解構** — 「外星人」作為語義壓縮概念、多來源模型集合（由原第六部分移入）

---

## 共同創作

本假說由以下 AI 模型與工具協助共同創作：

**AI 模型：**
- [GPT-5](https://openai.com/)（OpenAI）
- [Claude Opus 4](https://anthropic.com/)（Anthropic）

**工具：**
- [OpenClaw](https://github.com/openclaw/openclaw) — AI 閘道器與代理人執行環境
- [Claude Code](https://claude.ai/claude-code) — Anthropic 的代理人編程工具

---

## 協作說明

- [CONTRIBUTING.md](./CONTRIBUTING.md) — 貢獻流程、證據標準與 PR 檢查清單
- [BUILD.md](./BUILD.md) — 本機安裝、可選的本機 PDF 建置與可重跑驗證指令
- [`verification/verification.json`](./verification/verification.json) — 最新機器可讀參考文獻稽核結果
- [`verification/verification.csv`](./verification/verification.csv) — 最新平面化參考文獻稽核匯出

## 三份文檔同步規則

- `markdown/en/hypothesis-en.md` 是英文內容的工作主稿，適合日常修文與 AI 協作。
- `markdown/zh-TW/hypothesis-zh-TW.md` 是正體中文內容的工作主稿，適合日常修文與 AI 協作。
- `latex/main.tex` 是準備正式 PDF 時使用的排版來源，主要配合 Overleaf 工作流。
- 已編譯 PDF 不納入版本控制；需要時由 Overleaf 匯出。
- 若一次修改涉及結構、引用或跨語言內容，請盡量在同一個 PR 內同步相關 Markdown 與 LaTeX，或明確註記尚待同步的部分。

## PDF 工作流

這個專案的主要 PDF 流程如下：

1. 先在 repo 內維護 Markdown 與 LaTeX 原始檔。
2. 將 LaTeX 內容同步到 Overleaf。
3. 在 Overleaf 中搭配 Claude Browser Extension 協作最後的 PDF 導向修訂。
4. 需要 PDF 時再從 Overleaf 匯出。

Repository 保留的是可編輯來源檔，不追蹤已編譯 PDF。

## 可重跑驗證

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 scripts/verify_references.py
```

這會從 `latex/references.bib` 重新產生機器可讀的驗證輸出。

---

## 授權

本作品採用 [Creative Commons 姓名標示 4.0 國際授權條款 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.zh-hant) 授權。

您可以自由分享與改作本作品，惟須適當標註出處。Repository 層級的授權聲明請見根目錄 [LICENSE](./LICENSE)。
