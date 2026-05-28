import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from model_training import train_model


def evaluate_model(y_test, y_pred):

    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(
        y_test,
        y_pred,
        average='weighted'
    )

    recall = recall_score(
        y_test,
        y_pred,
        average='weighted'
    )

    f1 = f1_score(
        y_test,
        y_pred,
        average='weighted'
    )

    print("\nModel Evaluation Metrics\n")

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1-Score : {f1:.4f}")

    print("\nClassification Report\n")
    print(classification_report(y_test, y_pred))

    print("\nConfusion Matrix\n")
    print(confusion_matrix(y_test, y_pred))


if __name__ == "__main__":

    # Load dataset
    df = pd.read_csv(
        'data/processed_data/featured_supply_chain.csv'
    )

    # Train model
    model, X_test, y_test, y_pred = train_model(df)

    # Evaluate model
    evaluate_model(y_test, y_pred)