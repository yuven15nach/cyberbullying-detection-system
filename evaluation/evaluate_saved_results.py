import pandas as pd

from evaluation.metrics import (
    evaluate_bullying,
    evaluate_type
)

results = pd.read_csv("evaluation/evaluation_results.csv")

y_true_binary = results["Actual_Bullying"]
y_pred_binary = results["Predicted_Bullying"]

y_true_type = results["Actual_Type"]
y_pred_type = results["Predicted_Type"]

evaluate_bullying(y_true_binary, y_pred_binary)
evaluate_type(y_true_type, y_pred_type)