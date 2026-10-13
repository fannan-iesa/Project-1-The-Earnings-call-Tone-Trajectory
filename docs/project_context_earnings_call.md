# Project Context — Earnings-Call Tone-Trajectory Detector

> Scope: this project only. Last updated Oct 12, 2026. Edit the checklist and "Open decisions" as things change.

## Who I am (only what matters here)
- 2nd-year B.Tech CSE (Data Science), Jamia Millia Islamia, Delhi. Goal: GCC internship → full-time in AI/ML + platform engineering (BFSI GCCs especially).
- This is **Project 2** of a 4-project portfolio roadmap (1: credit-risk predictor, in progress · 3: full-stack product · 4: RBI/SEBI circular RAG assistant).
- **Starting level: zero deep learning.** I am learning DL and building simultaneously, one concept + one build task per day. Classical ML is in progress (ISL, Hands-On ML). DSA (Striver, C++) runs daily in parallel and must not be deprioritized.

## The project in one paragraph
Take earnings-call transcripts, split each into chunks (prepared remarks vs. Q&A, speaker-tagged), score the sentiment of every chunk, and turn the scores into a **trajectory** across the call. Then test whether the *shape* of that trajectory predicts post-call market volatility better than a single average sentiment score does.

## Hypothesis (write this in the README too)
Tone *trajectory* features (prepared-vs-Q&A tone drop, within-Q&A tone volatility, min/max chunk score, section-to-section deltas) predict next-day volatility / absolute return better than a static average sentiment score.

## Why this is a real problem (verify before citing publicly)
- Prior research finds Q&A tone is more informative than scripted prepared remarks because it is unscripted. Related work: Stanford GSB study on manager evasiveness in Q&A predicting later earnings misses; a 2025 *Financial Review* paper on "tone distance" between executives; a 2026 REIT study testing Q&A vs. presentation tone against volatility.
- Alt-data vendors sell earnings-call NLP signals commercially, so this is not purely academic.

## Pipeline (stages)
1. Environment, repo skeleton, MLflow set up.
2. Classical sentiment baselines on Financial PhraseBank.
3. DL fundamentals from zero (NumPy MLP, backprop by hand, PyTorch).
4. Attention from scratch → small encoder-only transformer sentiment classifier.
5. Comparison table of scorers (below).
6. Transcript collection + parsing into speaker-tagged chunks.
7. Chunk scoring → trajectory features.
8. Align with market data (strictly no lookahead) → build target.
9. Static-baseline vs. trajectory regression + significance test.
10. Writeup, tests, README. Then Phase 8 platform extension.

## Sentiment scorers being compared
| # | Scorer | Role |
|---|---|---|
| 1 | Loughran-McDonald lexicon | Classical baseline #1 (finance-specific word list) |
| 2 | TF-IDF + Logistic Regression / SVM | Classical baseline #2 |
| 3 | My from-scratch transformer encoder | The DL-learning centerpiece |
| 4 | FinBERT (`ProsusAI/finbert`) | Transfer-learning comparison |
| 5 | Zero-shot LLM via API | Modern comparison (research on LLM-vs-FinBERT is mixed, so this is a genuine test) |

Honest expectation: a classical or pretrained model may beat my scratch transformer on a small labeled set. That is an acceptable, reportable result.

## Data
- Sentiment training: Financial PhraseBank (sentence-level financial news). **Domain-shift caveat:** it is news text, not spoken call language. State this as a limitation.
- Transcripts: ~20–30 companies × several quarters to start. Source TBD (see open decisions).
- Market data: `yfinance` daily prices. Intraday NSE data is mostly paywalled, so use daily OHLC-based volatility proxies if I go the Indian-market route.

## Evaluation plan
- Scorer quality: accuracy, macro-F1, confusion matrix on a held-out PhraseBank test set.
- Hypothesis test: MAE / RMSE / R² for static-average model vs. trajectory model, **time-aware split** (train on earlier quarters, test on later ones), plus a paired **bootstrap significance test** on the error difference. If the target is a variance/volatility proxy, consider QLIKE loss.
- Optional extra check: does the signal add anything beyond pre-earnings implied volatility or analyst-estimate dispersion?
- Ablation: run the downstream hypothesis test with each scorer (not only my scratch model).

## Traps to guard against
- **Lookahead bias:** transcript release time vs. market data timestamps. Must have an explicit test/assertion that catches leakage.
- Tiny dataset → overfitting. Use regularization and report uncertainty, not just point estimates.
- Cherry-picking: log every run in MLflow; report where baselines win.
- Data licensing: check terms of service/robots.txt for any scraped transcript source and the license on Financial PhraseBank before publishing data in the repo.
- Never commit API keys (LLM API) — `.env` + `.gitignore`.

## Tooling
Python 3.11+, git, venv/conda, PyTorch, scikit-learn, pandas, Hugging Face `transformers`/`tokenizers`, MLflow, `yfinance`, pytest, spaCy (preprocessing). Phase 8: FastAPI + Pydantic, Docker/docker-compose, one cloud (AWS or Azure), GitHub Actions, optionally Airflow, Streamlit/Gradio frontend.

## Repo structure
`data/` (raw, processed; gitignored) · `notebooks/` · `src/` · `tests/` · `models/` (gitignored or tracked via DVC) · `docs/` · `README.md` · `requirements.txt`

## Progress checklist
- [ ] Phase 0 — env, repo, MLflow, data source scouting
- [ ] Phase 1 — classical NLP baselines
- [ ] Phase 2 — DL fundamentals (backprop by hand, PyTorch)
- [ ] Phase 3 — attention/transformer block from scratch
- [ ] Phase 4 — train scratch transformer; FinBERT + LLM comparison
- [ ] Phase 5 — transcript pipeline + leakage guard
- [ ] Phase 6 — static vs. trajectory hypothesis test
- [ ] Phase 7 — writeup, tests, README
- [ ] Phase 8 (optional now / else defer to Project 3) — FastAPI → Docker → cloud → CI/CD → Airflow → monitoring

Curriculum mapping: Phases 1–7 ↔ Milestones 1.2, 1.6–1.8, 2.1–2.5; Phase 8 ↔ 2.6, 2.7, 3.5, 3.7, 4.9, 4.11.

## Standing decisions
- Build self-attention and backprop **by hand** (non-negotiable learning items), then use PyTorch.
- Always include the classical baselines and the significance test; honest results beat flashy ones.
- Protect Phases 1–6; trim visuals and Phase 8 stretch items first if behind schedule.

## Open decisions
- Company universe: US large-caps (easier transcripts) vs. Indian listed companies (more on-brand for GCC/India). Not decided.
- Transcript source (license/ToS-clean dataset vs. scraping).
- Target variable: next-day absolute return vs. volatility proxy; horizon (1-day vs. 3-day).
- Which scorer feeds the downstream model (decide after Phase 4 results).
- Whether to do Phase 8 now or reuse it for Project 3.

## How I want Claude to help on this project
- Explain every concept from zero before using it; define jargon on first use.
- On 🔴 IMPLEMENT steps (backprop, self-attention), give hints and review my code before handing over full solutions.
- Be honest about weak results and small-sample limits; do not oversell.
- Give one day's task at a time unless I ask for more; flag when a step is over- or under-scoped.
- Help me write professional commits and README prose, but let me draft in my own voice first.

## Re-verify before relying on
Dataset licenses, transcript source terms, library versions, and any research findings above before quoting them in the README.
