import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier


def train_model(df):

    # Drop unnecessary columns
    X = df.drop(
    columns=[
        'generated_risk_classification',
        'severity_level',
        'risk_classification',
        'timestamp'
    ],
    errors='ignore'
)

    # Target variable
    y = df['generated_risk_classification']

    # Encode target labels
    label_encoder = LabelEncoder()

    y = label_encoder.fit_transform(y)

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Initialize Random Forest Model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    # Train Model
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Save trained model
    joblib.dump(
        model,
        'models/risk_classification_model.pkl'
    )

    print("\nModel training completed successfully.")
    print("\nModel saved in models folder.")

    return model, X_test, y_test, y_pred


if __name__ == "__main__":

    # Load featured dataset
    df = pd.read_csv(
        'data/processed_data/featured_supply_chain.csv'
    )

    # Train model
    model, X_test, y_test, y_pred = train_model(df)

    # Print sample predictions
    print("\nSample Predictions:\n")
    print(y_pred[:10])