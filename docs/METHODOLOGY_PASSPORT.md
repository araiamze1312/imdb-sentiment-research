# Methodology Passport Card — Task 2

## 1. Project information

**Title:** Accuracy–Efficiency Trade-offs of Naive Bayes, Logistic Regression, and DistilBERT for IMDB Sentiment Classification

**Authors:** Amze Arailym; Bayan Valikhanova

**GitHub repository:** `https://github.com/araiamze1312/imdb-sentiment-research`

**Research question:** How do model architecture and training set size affect sentiment classification quality and computational cost on the IMDB dataset?

## 2. Research type

**Quantitative experimental research.** We will systematically vary model type and the number of training examples, then measure numeric test-set classification and computation metrics. This is not a qualitative study or a mixed-methods study.

## 3. Hypotheses

The following operational hypotheses refine the research questions in Task 1. Test-set performance will be summarized over five fixed random seeds; the official 25,000-review IMDB test set remains fixed.

- **RQ1 H0:** Mean accuracy improvement of DistilBERT over TF-IDF + Logistic Regression on IMDB is **at most 2 percentage points**.
- **RQ1 H1:** Mean accuracy improvement of DistilBERT over TF-IDF + Logistic Regression on IMDB is **more than 2 percentage points**.
- **RQ2 H0:** The DistilBERT-versus-Logistic-Regression accuracy gap does not change with the training sample size (1,000 / 5,000 / 25,000).
- **RQ2 H1:** The gap at 1,000 training reviews is larger than the gap at 25,000 reviews.
- **RQ3 H0:** Logistic Regression's mean accuracy per training minute is no greater than DistilBERT's.
- **RQ3 H1:** Logistic Regression's mean accuracy per training minute is greater than DistilBERT's.

The 2-percentage-point threshold is a pre-specified practical improvement criterion from Task 1. RQ1 uses a strict threshold in H1 so the two hypotheses are complementary. RQ2's stated H1 is directional; exploratory trends across all three sizes will also be described. Accuracy-per-minute is a descriptive efficiency proxy and will be interpreted cautiously when fitting times are very short.

## 4. Variable matrix

| Category | Variable | Operationalization |
|---|---|---|
| Independent | Classifier | TF-IDF + Multinomial Naive Bayes; TF-IDF + Logistic Regression; fine-tuned DistilBERT |
| Independent | Training set size | 1,000, 5,000 or 25,000 reviews, stratified subsamples from the same IMDB training split |
| Dependent | Accuracy | Correct predictions / 25,000 IMDB test reviews; reported as % |
| Dependent | F1 score | Binary F1 for positive reviews, 0 to 1 |
| Dependent | Training time | Wall-clock seconds or minutes from model fitting/fine-tuning |
| Dependent | Prediction time | Seconds per 1,000 test reviews; batch settings documented |
| Dependent | Accuracy gap | DistilBERT accuracy minus Logistic Regression accuracy, in percentage points |
| Dependent | Accuracy per minute | Test accuracy (percentage points) / training minutes, interpreted with caution |
| Controlled | Input data | IMDB English movie review dataset, predefined 25k train / 25k test; fixed test set |
| Controlled | Randomness | Five predeclared seeds and identical sampled review IDs within a run |
| Controlled | Environment | Hardware, operating system, Python and exact dependency versions recorded per run |
| Controlled | Evaluation | Same test set, label definitions and scoring implementation; no test data in training |
| Controlled | Training policy | Predeclare hyperparameters, epochs, batch sizes and preprocessing for each model; document justified model-specific differences |

## 5. Metrics and baseline

**Primary metric:** Mean **test accuracy (%)** across five repeats, especially the DistilBERT minus Logistic Regression gap in percentage points at 25,000 training reviews (RQ1).

**Secondary metrics:** F1 score, wall-clock training time, seconds per 1,000 test reviews, accuracy per minute, and 95% confidence intervals. For paired runs, use matched seeds and a paired comparison of accuracy differences; report the exact statistical procedure and assumptions.

**Guardrail metrics:** No failed runs or uncaught exceptions; no training/test leakage; record peak RAM and CPU utilization. Suggested resource limits for later full-scale runs are peak RAM <= 8,192 MB and peak CPU utilization <= 80% **when measured**. These limits are design targets, not demonstrated properties of the Week 6 script, and may need revision for DistilBERT/GPU experiments.

**Baseline:** TF-IDF + Logistic Regression, trained and evaluated on precisely the same subsets and test reviews. TF-IDF + Multinomial Naive Bayes is a second classical reference. DistilBERT is the proposed higher-complexity comparator.

## 6. Experimental procedure and Week 6 scope

1. **Week 6:** Validate a runnable measurement pipeline on `data/sample/imdb_micro.csv` (10 illustrative reviews). The executable prototype trains only **Naive Bayes and Logistic Regression** and measures accuracy, F1, fit and prediction time. Its outputs are smoke-test values, not research evidence.
2. **Week 7 onward:** Obtain the official IMDB dataset and record the original source, checksum/version, split and license. Produce shared stratified 1k/5k/25k training subsets, controlled by five recorded seeds.
3. Train the two classical baselines and add a separate pinned DistilBERT fine-tuning environment/script with documented tokenizer, weights revision, batch size, epochs and device.
4. Save one structured result per model, training size and seed. Capture hardware and resource measurements and any failures.
5. Aggregate scores and timing, compute uncertainty and statistical tests, and evaluate H0/H1 against the registered threshold.

**Scope note:** DistilBERT, the full IMDB download, repeat-run automation, and CPU/RAM instrumentation are planned for Week 7; they are not implemented in the Week 6 smoke-test repository. No full-study results are claimed here.
