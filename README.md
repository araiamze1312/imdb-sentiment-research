# IMDB Sentiment Classification: Accuracy and Time-Cost Benchmark

**Authors:** Amze Arailym and Bayan Valikhanova  
**Course deliverable:** Task 2 — Methodology Passport and Reproducible Research Repository (Weeks 5–6)

## Overview

This quantitative research project compares **TF-IDF + Naive Bayes**, **TF-IDF + Logistic Regression**, and the planned **fine-tuned DistilBERT** for binary sentiment classification on the IMDB dataset. The independent variables are model type and training-set size (1,000, 5,000, 25,000). The target outcomes are test accuracy, F1, training duration and prediction speed.

**Research question:** How do classifier choice and training set size affect accuracy and computational costs when predicting movie-review sentiment?

**Important scope:** The Week 6 implementation is a **working smoke test** on a synthetic 10-row sample using Naive Bayes and Logistic Regression. **DistilBERT fine-tuning and official IMDB runs are planned for Week 7.** Do not cite the micro-sample scores as experimental findings.

## System Requirements

- Docker Desktop with a running Docker engine, or Python 3.13 with pip
- Approximately 1 GB free space for Docker/dependencies (available space may vary)
- Network connection for the initial image/dependency installation
- CPU only for the Week 6 smoke test

## Quickstart (Docker: two commands)

From the repository folder:

```powershell
docker build -t imdb-benchmark .
docker run --rm imdb-benchmark
```

The second command prints JSON metrics and writes `results/sample_benchmark.json` **inside the temporary container**. Since `--rm` removes the container, stdout is the accessible result. To keep the file on Windows PowerShell, create a local `results` folder, then run:

```powershell
mkdir results
docker run --rm --mount "type=bind,source=$((Get-Location).Path)/results,target=/app/results" imdb-benchmark
```

## Quickstart (local Python)

```powershell
python -m pip install -r requirements.txt
python src/benchmark.py --config configs/config.json
```

This writes `results/sample_benchmark.json` locally. Windows users may need `py -3.13` instead of `python` if multiple versions exist.

## Repository Structure

```text
.
├── README.md
├── LICENSE
├── .gitignore
├── .dockerignore
├── Dockerfile
├── requirements.txt
├── configs/
│   └── config.json
├── data/
│   └── sample/
│       └── imdb_micro.csv
├── src/
│   └── benchmark.py
├── notebooks/
│   └── README.md
└── docs/
    └── METHODOLOGY_PASSPORT.md
```

## Planned Benchmark Matrix

| Model | Training samples | Repetitions | Accuracy (%) | F1 | Train time (s) | Inference (s / 1,000) |
|---|---:|---:|---|---|---|---|
| TF-IDF + Naive Bayes | 1,000 / 5,000 / 25,000 | 5 each | Planned | Planned | Planned | Planned |
| TF-IDF + Logistic Regression (baseline) | 1,000 / 5,000 / 25,000 | 5 each | Planned | Planned | Planned | Planned |
| Fine-tuned DistilBERT | 1,000 / 5,000 / 25,000 | 5 each | Planned | Planned | Planned | Planned |

## Configuration and Current Output

Edit `configs/config.json` to set the input file, output location and Week 6 model settings. The script reads a CSV with `text,label,split` fields, trains on `train` rows, evaluates on `test` rows, and saves accuracy, F1, training seconds and prediction seconds. All timings are hardware-dependent. `planned_training_sizes`, `planned_repetitions`, `planned_transformer`, and CPU/RAM guardrail limits record the future research design; they are **not activated** by the prototype.

## Methodology, Citation and License

Methodological details and H0/H1: [`docs/METHODOLOGY_PASSPORT.md`](docs/METHODOLOGY_PASSPORT.md).

Dataset planned for Week 7: Maas et al. (2011), *Learning Word Vectors for Sentiment Analysis*, ACL, https://aclanthology.org/P11-1015/ . The included micro-dataset contains original illustrative sentences, not redistributed IMDB reviews.

Software is made available under the [MIT License](LICENSE). If citing this student project, cite the authors, repository title, GitHub URL and access date; there is no DOI assigned.
