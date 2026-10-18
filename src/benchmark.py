"""Week 6 smoke-test benchmark; real IMDB comparisons are planned for Week 7."""
import argparse
import csv
import json
import platform
import time
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import sklearn

ROOT = Path(__file__).resolve().parent.parent


def run(config_path):
    with config_path.open(encoding="utf-8") as handle:
        config = json.load(handle)
    data_path = ROOT / config["dataset_path"]
    with data_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows or any(row.get("label") not in ("0", "1") for row in rows):
        raise ValueError("Sample must contain rows with binary labels 0 or 1")
    train = [r for r in rows if r["split"] == "train"]
    test = [r for r in rows if r["split"] == "test"]
    if not train or not test or len({r["label"] for r in train}) < 2:
        raise ValueError("Both splits and both training classes are required")
    x_train, y_train = [r["text"] for r in train], [int(r["label"]) for r in train]
    x_test, y_test = [r["text"] for r in test], [int(r["label"]) for r in test]
    output = {"status": "smoke_test_only_not_research_results",
              "dataset": str(data_path.relative_to(ROOT)), "train_count": len(train),
              "test_count": len(test), "python": platform.python_version(),
              "sklearn": sklearn.__version__, "results": []}
    for model_name in config["models"]:
        if model_name == "naive_bayes":
            classifier = MultinomialNB()
        elif model_name == "logistic_regression":
            classifier = LogisticRegression(max_iter=config["logistic_regression_max_iter"],
                                            random_state=config["random_seed"])
        else:
            raise ValueError("Unsupported Week 6 smoke-test model: " + model_name)
        model = Pipeline([("tfidf", TfidfVectorizer(max_features=config["tfidf_max_features"])),
                          ("classifier", classifier)])
        start = time.perf_counter()
        model.fit(x_train, y_train)
        train_seconds = time.perf_counter() - start
        start = time.perf_counter()
        predicted = model.predict(x_test)
        predict_seconds = time.perf_counter() - start
        output["results"].append({"model": model_name,
            "accuracy": round(float(accuracy_score(y_test, predicted)), 4),
            "f1": round(float(f1_score(y_test, predicted, zero_division=0)), 4),
            "training_seconds": round(train_seconds, 6),
            "prediction_seconds": round(predict_seconds, 6),
            "prediction_seconds_per_1000": round(predict_seconds / len(test) * 1000, 6)})
    out_path = ROOT / config["output_path"]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))
    print("Saved results to:", out_path)
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/config.json")
    arguments = parser.parse_args()
    run(ROOT / arguments.config)
