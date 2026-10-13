# Earnings-Call Tone-Trajectory Detector — Full Build Roadmap

*A day-by-day learn-then-build plan, from zero DL knowledge to a deployed, portfolio-ready project. Tagged against your two curriculum docs so you always know why you're doing each step.*

## How to use this
- Each day = one learning block (📘) and/or one build block (🛠️), sometimes an evaluation checkpoint (🧪). 🎯 marks an optimization we discussed earlier — don't skip these, they're what makes this project defensible, not generic. ⚙️ marks the platform-engineering extension (Phase 8).
- Check items off as `- [x]` as you go — this file is a working checklist, not just a read-once plan.
- If a day's concept takes two days instead of one, that's normal and fine. The *order* matters far more than the calendar. Don't compress Phase 2-3 (DL fundamentals) to catch up — that's the actual point of this project.
- Legend: 📘 Learn · 🛠️ Build · 🧪 Evaluate · 🎯 Optimization · ⚙️ Platform/DevOps

---

## Phase 0 — Environment & Project Skeleton (2-3 days)
*[Milestone 1.2 — Software Engineering Practice]*

- [ ] **Day 1 — Repo & environment setup.** Create a git repo with folders: `data/`, `notebooks/`, `src/`, `tests/`, `models/`. Set up a virtual environment (`venv` or `conda`), pin dependencies in `requirements.txt`. Write a skeleton `README.md` stating your hypothesis up front: *"Does the trajectory of sentiment across an earnings call predict next-day volatility better than a single average sentiment score?"* Writing this now, before any code, keeps you honest about what you're actually testing.
  - Tools: Python 3.11+, git, venv/conda, VS Code.
- [ ] **Day 2 — Experiment tracking skeleton.** Install MLflow locally, log one dummy run (any random number as a "metric") just to confirm the tracking setup works *before* you need it for real models.
  - Tools: `mlflow`. Concept: why you track experiments from day one, not retroactively.
- [ ] **Day 3 — Data source scouting.** Identify your transcript source (Motley Fool/Seeking Alpha free transcripts, SEC EDGAR 8-K exhibits, or an existing Kaggle earnings-call-transcript dataset). Pull 3-5 sample transcripts and confirm the format is usable before committing your data pipeline to it.
  - Deliverable: 3-5 raw transcripts saved in `data/raw/`.

---

## Phase 1 — Classical NLP Foundations & Baselines (Week 1)
*[Milestone 2.4 (EXPLAIN/AWARENESS parts), 1.2]*

- [ ] **Day 1.** 📘 Learn tokenization, stopword removal, lemmatization (conceptually — a spaCy quickstart is enough). 🛠️ Write a text-cleaning function for transcripts. Keep punctuation and capitalization if you can — tone signals sometimes live there.
- [ ] **Day 2.** 📘 Learn Bag-of-Words and TF-IDF. 🛠️ Vectorize a batch of Financial PhraseBank sentences with `scikit-learn`'s TF-IDF vectorizer.
- [ ] **Day 3.** 📘 Learn the **Loughran-McDonald finance sentiment dictionary** — why general-English sentiment lexicons fail on financial text (words like "liability," "tax," "cost" read as negative generally but are neutral or routine in finance). 🛠️ Download the LM word list, write a simple lexicon-scoring function (count positive/negative words per document). **This is Classical Baseline #1.**
- [ ] **Day 4.** 🛠️ Train a classical ML sentiment classifier (Logistic Regression or SVM on TF-IDF) on the Financial PhraseBank dataset. 🧪 Evaluate with accuracy/F1/confusion matrix (Milestone 1.8 — you already know these). **This is Classical Baseline #2.**
- [ ] **Day 5.** 🛠️ Wrap both baselines into one clean, reusable evaluation script; log both to MLflow. 🎯 Write down these numbers now — this is the bar your transformer has to clear later, and it's fine if it doesn't clear it immediately.

---

## Phase 2 — Deep Learning Fundamentals From Zero (Week 2)
*[Milestone 2.1-2.2]*

- [ ] **Day 1.** 📘 Perceptron, weights/bias, activation functions (ReLU, sigmoid, softmax). Resource: 3Blue1Brown's neural network series is the best visual intuition; cross-reference with the DL chapter in ISL you're already using.
- [ ] **Day 2.** 📘 Forward pass + loss functions (cross-entropy for classification). 🛠️ Implement a tiny 2-layer MLP in **raw NumPy** on a toy (non-financial) dataset — the point is mechanics, not the data.
- [ ] **Day 3.** 📘 Backpropagation and the chain rule. 🛠️ **Manually derive and code backprop** for your Day-2 NumPy MLP — no autograd yet. This is the specific "implement backprop by hand once" exercise your curriculum calls for; don't skip it.
- [ ] **Day 4.** 📘 Optimizers: SGD, Momentum, Adam; learning rate intuition. 🛠️ Swap optimizers on your toy MLP, observe convergence differences.
- [ ] **Day 5.** 📘 PyTorch basics: tensors, autograd, `nn.Module`, `DataLoader`. 🛠️ Reimplement your Day 2-4 MLP in PyTorch — this should make it click exactly what autograd is automating for you.
- [ ] **Day 6.** 📘 Regularization: dropout, weight decay, early stopping — and *why* your small earnings-call dataset will need these later. 🛠️ Add dropout to the PyTorch MLP, watch the train/validation gap change.

---

## Phase 3 — Sequence Models & Attention (Week 3)
*[Milestone 2.4-2.5 — the pedagogical core of this whole project]*

- [ ] **Day 1.** 📘 Why plain feedforward nets fail on sequences; RNN/LSTM/GRU intuition only (you do not need to implement these — your curriculum marks this EXPLAIN-level). Resource: Chris Olah's "Understanding LSTMs" is the classic, still-best intuitive explainer.
- [ ] **Day 2.** 📘 The attention mechanism: query/key/value, why it beats compressing a whole sequence into one fixed vector. Resource: Raschka's self-attention-from-scratch article (already in your curriculum's reference list).
- [ ] **Day 3.** 🛠️ Implement **single-head self-attention from scratch** on a toy sequence of a handful of word embeddings — pure mechanics, no real data yet.
- [ ] **Day 4.** 📘 Multi-head attention and positional encoding. 🛠️ Extend Day 3 to multi-head attention.
- [ ] **Day 5.** 📘 Encoder-only (BERT-style) vs. decoder-only (GPT-style) vs. encoder-decoder (T5) — conceptual distinction only. 🛠️ Assemble a minimal transformer encoder block: attention + feedforward + layer norm + residual connections. This is your model architecture skeleton for Phase 4.

---

## Phase 4 — Train Your From-Scratch Sentiment Transformer (Week 4)

- [ ] **Day 1.** 📘 Basic tokenization for real text (a simple whitespace + vocabulary tokenizer is fine for v1 — don't over-engineer this early). 🛠️ Build a vocabulary from Financial PhraseBank and tokenize the dataset.
- [ ] **Day 2.** 🛠️ Wire your Phase-3 encoder block into a classifier: encoder → [CLS]-style pooling → linear head → 3-class sentiment output. Write the training loop.
- [ ] **Day 3.** 🛠️ Train on Financial PhraseBank, log every run to MLflow (loss curves, accuracy). Budget the whole day for debugging — a first training loop rarely converges on the first try, and that's normal, not a sign you're doing it wrong.
- [ ] **Day 4.** 🧪 Evaluate your transformer against the Phase-1 classical baselines on a held-out test set. 🎯 If a classical baseline wins here, that's a genuinely honest and expected result on a small labeled dataset — note it for your writeup rather than treating it as a failure.
- [ ] **Day 5.** 📘 Transfer learning for NLP. 🛠️ Load **FinBERT** (`ProsusAI/finbert` on Hugging Face), run it on the same test set. This is comparison point #3.
- [ ] **Day 6.** 🎯 Build the **zero-shot LLM comparison**: prompt an LLM API (Claude/GPT) to score the same test sentences, log its accuracy. You now have four models compared on one table: lexicon, classical ML, your from-scratch transformer, FinBERT, and zero-shot LLM — a genuinely rich comparison most student projects never build.

---

## Phase 5 — Earnings Call Data Pipeline (Week 5)

- [ ] **Day 1.** 📘 Basic scraping/API sourcing (`requests`, `BeautifulSoup`, or an existing dataset). 🛠️ Collect transcripts for ~20-30 companies across a few quarters each — a realistic target given your timeline.
- [ ] **Day 2.** 🛠️ Parse transcripts into structured, speaker-tagged sections: prepared remarks vs. Q&A. Expect real formatting inconsistencies across sources — this is genuine data engineering, not a solved problem.
- [ ] **Day 3.** 🛠️ Run your trained sentiment scorer (Phase 4) over every chunk of every transcript to produce a raw sentiment sequence per call.
- [ ] **Day 4.** 🛠️ Engineer trajectory features: prepared-vs-Q&A tone drop, within-Q&A tone volatility (std. dev. of chunk scores), min/max chunk score, section-to-section deltas.
- [ ] **Day 5. ⚠️ Critical day.** 📘 Lookahead bias specific to this data — transcript release timestamp vs. market data timestamp. 🛠️ Pull matching stock return data (`yfinance`) and align timestamps so you only ever use information available *before* your prediction window. Write an explicit test/assertion that catches leakage — this is the single most common mistake in this kind of project, and the exact "what's wrong with this validation setup" trap your curriculum already flags for time series generally.

---

## Phase 6 — Predicting Volatility From the Trajectory (Week 6)
*[Milestone 1.6-1.7]*

- [ ] **Day 1.** 📘 Realized volatility / return-based target construction. 🛠️ Compute next-day (and optionally next-3-day) absolute return or volatility per transcript event.
- [ ] **Day 2.** 🛠️ **Static baseline**: predict the target from the single average sentiment score only, via Linear Regression.
- [ ] **Day 3.** 🛠️ **Trajectory model**: predict the target from your full trajectory feature set (or feed the raw per-chunk sequence into a small model). Compare against Day 2.
- [ ] **Day 4.** 🧪 Evaluate both with MAE/RMSE/R². 🎯 Run a bootstrap significance test comparing the two models' errors — this comparison is the actual hypothesis test at the center of your whole project, so don't skip the statistics and just eyeball which number is smaller.
- [ ] **Day 5 (if time allows).** 🎯 Pull pre-earnings implied volatility or analyst-estimate dispersion as an extra check: does your trajectory signal add anything beyond what the market already prices in? A negative or mixed result here is a sophisticated, honest finding — not a failure.

---

## Phase 7 — Packaging, Interpretability & Writeup (Week 7)

- [ ] **Day 1.** 🛠️ Consolidate every baseline, your model, and your statistical tests into one clean comparison table/notebook.
- [ ] **Day 2.** 🛠️ Visualize a few example sentiment-over-call-time trajectories per company — this single chart type is genuinely great demo material for a README or interview screen-share.
- [ ] **Day 3.** 📝 Write the project README: hypothesis, data, method, **honest** results (including anywhere a classical baseline won), limitations (small sample size, how you handled lookahead bias, whether the LLM zero-shot comparison was or wasn't competitive).
- [ ] **Day 4-5.** Clean up the repo structure; add `pytest` tests for your pipeline functions (Milestone 1.2 habit) — at minimum, test the lookahead-bias guard and the trajectory-feature computation, since those are the two places a silent bug would be most damaging.

---

## Phase 8 — Platform Engineering Extension (Week 8+)
*This is what turns a notebook into a "Full-Stack DS / Platform Engineer" portfolio piece — directly answers your DevOps/SDE question.*

- [ ] **Day 1.** ⚙️ *[Milestone 3.5]* Wrap your trained model + trajectory pipeline in a **FastAPI** backend: one endpoint that takes a transcript (or ticker + quarter) and returns the sentiment trajectory + volatility prediction. Learn: REST basics, Pydantic request/response schemas.
- [ ] **Day 2.** ⚙️ Add basic API-key auth and rate limiting to the service (also flagged in Milestone 3.5).
- [ ] **Day 3.** ⚙️ *[Milestone 2.6]* Containerize with Docker — write a Dockerfile for the FastAPI service + model artifact, use a multi-stage build to keep the image small, test locally with `docker-compose`.
- [ ] **Day 4.** ⚙️ *[Milestone 2.7]* Deploy the container to a cloud compute instance or managed container service (AWS ECS / Azure Container Instances) — pick one cloud, practice IAM basics, and remember to shut the instance down after testing so you don't burn credits.
- [ ] **Day 5.** ⚙️ *[Milestone 3.5]* Build a minimal frontend — a Streamlit or Gradio app is an explicitly legitimate substitute per your curriculum — that calls your FastAPI backend and displays the trajectory chart.
- [ ] **Day 6.** ⚙️ *[Milestone 3.7]* Set up CI/CD: a GitHub Actions workflow that runs `pytest` and lint on every push, optionally auto-building and pushing the Docker image.
- [ ] **Day 7 (stretch).** ⚙️ *[Milestone 4.9]* Wrap the data pipeline (scrape new transcripts → score sentiment → predict → store result) as an **Airflow DAG**: ingestion → feature computation → prediction → result storage. This is a direct, hands-on demonstration of the pipeline-orchestration skill your curriculum flags at Milestone 4.9.
- [ ] **Day 8 (stretch).** ⚙️ *[Milestone 4.11]* Add basic monitoring: log every prediction request, and track whether the distribution of incoming sentiment scores is drifting from your training distribution over time — even simple logging-based drift tracking counts here.

### A strategic note on Phase 8
You have a real choice here, and it's worth making deliberately rather than by default: **do Phase 8 now** to make this project your full-stack + platform showcase, or **defer these exact skills to your existing Project 3 slot**, which already plans full-stack + K8s + CI/CD work. If you do Phase 8 here, Project 3 can skip re-learning FastAPI/Docker from scratch and go deeper (real Kubernetes, more elaborate CI/CD, a second model) instead of repeating groundwork. Either is defensible — just don't do the introductory version of this twice.

---

## Curriculum cross-reference (quick lookup)

| Phase | What it covers | Milestone(s) |
|---|---|---|
| 0 | Repo hygiene, environment, tracking | 1.2 |
| 1 | Classical NLP, TF-IDF, lexicon baseline | 2.4 (EXPLAIN/AWARENESS), 1.8 |
| 2 | DL fundamentals from zero | 2.1-2.2 |
| 3 | Sequence models, attention from scratch | 2.4-2.5 |
| 4 | Transformer training, transfer learning, LLM comparison | 2.4-2.5 |
| 5 | Data pipeline, lookahead-bias discipline | 1.6 |
| 6 | Trajectory-vs-static hypothesis test | 1.6-1.7 |
| 7 | Interpretability, writeup, testing | 1.2 |
| 8 | FastAPI, Docker, cloud, CI/CD, Airflow, monitoring | 2.6, 2.7, 3.5, 3.7, 4.9, 4.11 |

## If you fall behind schedule — what to cut, in order
1. **Never cut:** Phases 1-6 (the actual ML project and its hypothesis test) or the backprop-by-hand and self-attention-from-scratch exercises in Phases 2-3 — these are exactly what an interviewer will probe, and skipping them defeats the point of this being your DL-learning vehicle.
2. **Trim first:** Phase 7's extra visualizations (keep the writeup, cut extra charts).
3. **Trim second:** Phase 8's stretch items (Airflow, monitoring) — FastAPI + Docker + cloud deploy (Phase 8, Days 1-4) is the minimum bar for "full-stack" credibility; CI/CD and Airflow are genuine bonuses, not requirements.
