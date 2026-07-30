import pandas as pd
import csv

from detectors.rule_based import classify_rule_based
from utils.preprocessing import clean_text

from evaluation.metrics import (
    evaluate_bullying,
    evaluate_type
)


data = pd.read_csv("data/cyberbullying_tweets.csv")

NUM_SAMPLES = 200

data = data.sample(
    n=NUM_SAMPLES,
    random_state=42
).reset_index(drop=True)


y_true_binary = []
y_pred_binary = []

y_true_type = []
y_pred_type = []

results = []


for i in range(len(data)):

    text = clean_text(
        data.iloc[i]["tweet_text"]
    )

    actual_type = str(
        data.iloc[i]["cyberbullying_type"]
    ).lower()

    actual_binary = (
        "No"
        if actual_type == "not_cyberbullying"
        else "Yes"
    )

    prediction = classify_rule_based(text)

    predicted_binary = prediction["bullying"]
    predicted_type = prediction["type"]

    y_true_binary.append(actual_binary)
    y_pred_binary.append(predicted_binary)

    y_true_type.append(actual_type)
    y_pred_type.append(predicted_type)

    results.append([
        text,
        actual_binary,
        predicted_binary,
        actual_type,
        predicted_type
    ])

    print(f"Processed {i+1}/{len(data)}")


with open(
    "evaluation/evaluation_results_rule_based.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.writer(f)

    writer.writerow([
        "Text",
        "Actual_Bullying",
        "Predicted_Bullying",
        "Actual_Type",
        "Predicted_Type"
    ])

    writer.writerows(results)


print("\nRule-based results saved.\n")


evaluate_bullying(
    y_true_binary,
    y_pred_binary
)

evaluate_type(
    y_true_type,
    y_pred_type
)