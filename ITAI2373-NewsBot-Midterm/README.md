# NewsBot Intelligence System — ITAI 2373 Mid-Term Project

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/denisbosire97-ai/Denis-Aosa-AI-Portfolio/blob/main/ITAI2373-NewsBot-Midterm/Midterm_NewsBot_Denis_Aosa_ITAI_2373.ipynb)

- **Author:** Denis Aosa (`denisbosire97-ai`) — Individual Submission
- **Course:** ITAI-2373: Natural Language Processing (Fall 2026)
- **Instructor:** Prof. Sridhar Ganti | Houston Community College
- **Portfolio Folder:** [`denisbosire97-ai/Denis-Aosa-AI-Portfolio/ITAI2373-NewsBot-Midterm`](https://github.com/denisbosire97-ai/Denis-Aosa-AI-Portfolio/tree/main/ITAI2373-NewsBot-Midterm)

---

## Project Overview

The **NewsBot Intelligence System** is an end-to-end Natural Language Processing (NLP) pipeline integrating **Modules 1–8** of ITAI-2373 to transform raw unstructured news articles into structured, queryable media intelligence. Executed and benchmarked in Google Colab across **1,200 balanced BBC News articles**, the system performs automated text normalization, TF-IDF lexical modeling, Penn Treebank POS profiling, `spaCy` syntactic dependency parsing, VADER sentiment analysis, multi-model classification benchmarking, and Named Entity Recognition (NER).

### Core System Capabilities
1. **Multi-Stage Text Preprocessing (Module 2):** Strips HTML markup, URLs, emails, and punctuation; applies NLTK tokenization, English stop-word filtering, and WordNet lemmatization (`46.0%` word-count reduction across the corpus).
2. **TF-IDF Lexical Feature Extraction (Module 3):** Extracts `5,000` unigram and bigram features (`min_df=2`, `max_df=0.8`, `97.43%` sparsity) and profiles distinctive domain vocabulary across 5 news verticals.
3. **Grammatical & Syntactic Profiling (Modules 4–5):** Quantifies `43` Penn Treebank POS tags across categories and extracts syntactic noun chunks, nominal subjects (`nsubj`), and objects (`dobj`/`pobj`) via `spaCy` (`en_core_web_sm`).
4. **Sentiment & Emotional Tone Analysis (Module 6):** Computes VADER compound, positive, neutral, and negative valence scores for headlines and full articles across categories.
5. **Multi-Class Classification Engine (Module 7):** Combines `5,000` TF-IDF features with non-negative scaled VADER sentiment (`4` features) and leak-free `MinMaxScaler` document-length features (`3` features) to benchmark `MultinomialNB`, `LogisticRegression`, and Linear `SVC` with 5-fold stratified cross-validation.
6. **Named Entity Recognition (Module 8):** Extracts and indexes `35,116` entity mentions (`10,676` unique entities across `18` labels including `DATE`, `PERSON`, `GPE`, `ORG`, and `MONEY`).
7. **Production Pipeline Class:** Encapsulates preprocessing, classification, confidence-based human-in-the-loop routing, sentiment scoring, and entity extraction inside `NewsBotIntelligenceSystem`.

---

## Dataset Summary

- **Source Corpus:** Curated BBC News Classification Corpus (`news_dataset.csv`)
- **Total Articles:** `1,200` English full-text articles (`0` missing values across all `6` columns: `article_id`, `title`, `content`, `category`, `date`, `source`)
- **Class Balance:** Perfectly balanced across **5 categories** (`240` articles each): `Business`, `Entertainment`, `Politics`, `Sports`, and `Technology`
- **Article Length:** Mean `2,296.4` characters (`min = 497`, `max = 25,216`) and `401.8` content words (`min = 90`, `max = 4,492`)
- **Train / Test Split:** Stratified `80/20` split (`960` training articles / `240` held-out test articles, `48` test articles per class)

---

## Empirical Results (Executed in Google Colab)

### 1. Multi-Class Classifier Benchmark (`5,007` Combined Features)

| Model | Test Accuracy (`N=240`) | 5-Fold CV Mean (`N=960`) | 5-Fold CV Std | Macro F1 |
|---|---:|---:|---:|---:|
| **Multinomial Naive Bayes (`MultinomialNB`)** | **97.08%** (`0.9708`) | **96.67%** (`0.9667`) | `0.0150` | **0.97** |
| **Linear SVM (`SVC(kernel='linear')`)** | **97.08%** (`0.9708`) | **96.56%** (`0.9656`) | `0.0142` | `0.97` |
| **Logistic Regression (`max_iter=1000`)** | **96.25%** (`0.9625`) | **95.63%** (`0.9562`) | `0.0134` | `0.96` |

- **Per-Class Performance (`MultinomialNB`):** `Sports` (`1.00` F1), `Entertainment` (`0.97` F1), `Politics` (`0.97` F1), `Business` (`0.96` F1), `Technology` (`0.96` F1).

### 2. Cross-Category Sentiment & Entity Profile

| Category | Mean VADER Compound | Positive % | Negative % | Top TF-IDF Terms | Total Entities |
|---|---:|---:|---:|---|---:|
| **Sports** | `+0.6164` | `81.67%` | `17.92%` | `england`, `game`, `win`, `cup`, `player` | `7,615` |
| **Entertainment** | `+0.6041` | `80.83%` | `19.17%` | `film`, `award`, `best`, `show`, `star` | `6,849` |
| **Technology** | `+0.5191` | `76.25%` | `22.92%` | `game`, `technology`, `people`, `mobile`, `user` | `6,158` |
| **Business** | `+0.1827` | `59.58%` | `39.58%` | `growth`, `economy`, `firm`, `company`, `bank` | `7,772` |
| **Politics** | `+0.1199` | `56.25%` | `42.92%` | `labour`, `blair`, `election`, `party`, `tory` | `6,722` |

---

## Repository Structure

```text
ITAI2373-NewsBot-Midterm/
├── Midterm_NewsBot_Denis_Aosa_ITAI_2373.ipynb          # Complete executed Colab notebook (all 22 code cells + 7 plots)
├── news_dataset.csv                                    # Curated 1,200-article balanced BBC News dataset
├── MT_Report_Group_Individual_Denis_Aosa_ITAI2373.pdf  # 4-page Technical & Business Intelligence Report
├── NewsBot_Reflection_Denis_Aosa.pdf                   # 2-page Reflective Journal (6 required sections)
└── README.md                                           # Project overview, empirical metrics, and quickstart guide
```

---

## Quickstart (Google Colab or Local Jupyter)

1. Click the **Open in Colab** badge at the top of this README (or open `Midterm_NewsBot_Denis_Aosa_ITAI_2373.ipynb` in JupyterLab).
2. Run **`Runtime -> Run all`**.
   - Cell 2 installs `spacy`, `scikit-learn`, `nltk`, `pandas`, `matplotlib`, `seaborn`, `wordcloud`, `plotly`, and `en_core_web_sm`.
   - Cell 5 automatically loads `news_dataset.csv` locally if present or fetches it directly from this GitHub repository (with an automatic raw BBC corpus fallback).

---

## Individual Contributions (`Denis Aosa`)

Completed individually per instructor approval (`Prof. Sridhar Ganti`). Denis Aosa designed, implemented, debugged, executed, and documented all system components end-to-end:
- Curated and validated the balanced `1,200`-article BBC News dataset (`news_dataset.csv`) with 3-tier reproducible Colab loading.
- Implemented Modules 1–8 (`clean_text`, `preprocess_text`, `TfidfVectorizer` + category visualizations, Penn Treebank POS heatmaps, `spaCy` dependency extraction, VADER valence analysis, leak-free multi-feature classification with 5-fold CV, and `nlp.pipe` NER extraction).
- Built and tested the `NewsBotIntelligenceSystem` pipeline class on unseen cross-domain articles and authored the technical report and 2-page reflective journal.
