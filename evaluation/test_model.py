import pandas as pd
import csv
import time

from evaluation.evaluate_classifier import classify_for_evaluation
from utils.preprocessing import clean_text
from evaluation.parse_output import parse_prediction

from evaluation.metrics import (
    evaluate_bullying,
    evaluate_type
)


# Load Dataset
data = pd.read_csv("data/cyberbullying_tweets.csv")

# Number of samples for evaluation
NUM_SAMPLES = 200

# Randomly select 200 samples
data = data.sample(
    n=NUM_SAMPLES,
    random_state=42
).reset_index(drop=True)


# Lists for Evaluation
y_true_binary = []
y_pred_binary = []

y_true_type = []
y_pred_type = []

results = []

# Evaluation Loop
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

    prediction = None

    try:
        prediction_raw = classify_for_evaluation(text)

        # Wait 5 seconds to respect Gemini 3.1 Flash Lite RPM limit
        time.sleep(5)

        prediction = parse_prediction(prediction_raw)

    except Exception as e:
        print(f"Error at sample {i+1}: {e}")
        continue

    if prediction is None:
        continue

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


# Save Results
with open(
    "evaluation/evaluation_results.csv",
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

print("\nResults saved.\n")


# Evaluation Metrics
evaluate_bullying(
    y_true_binary,
    y_pred_binary
)

evaluate_type(
    y_true_type,
    y_pred_type
)