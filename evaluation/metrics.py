from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import matplotlib.pyplot as plt
import seaborn as sns


def evaluate_bullying(y_true, y_pred):

    print("\n==========")
    print("BULLYING DETECTION")
    print("==========")

    print(
        "Accuracy:",
        accuracy_score(
            y_true,
            y_pred
        )
    )

    print(
        classification_report(
            y_true,
            y_pred,
            zero_division=0
        )
    )

    cm = confusion_matrix(
        y_true,
        y_pred
    )

    plt.figure(figsize=(5,4))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d"
    )

    plt.title(
        "Bullying Detection"
    )

    plt.xlabel(
        "Predicted"
    )

    plt.ylabel(
        "Actual"
    )

    plt.show()


def evaluate_type(y_true, y_pred):

    print("\n==========")
    print("TYPE CLASSIFICATION")
    print("==========")

    print(
        "Accuracy:",
        accuracy_score(
            y_true,
            y_pred
        )
    )

    print(
        classification_report(
            y_true,
            y_pred,
            zero_division=0
        )
    )

    cm = confusion_matrix(
        y_true,
        y_pred
    )

    plt.figure(figsize=(8,6))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d"
    )

    plt.title(
        "Cyberbullying Type Classification"
    )

    plt.xlabel(
        "Predicted"
    )

    plt.ylabel(
        "Actual"
    )

    plt.show()