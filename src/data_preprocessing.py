import pandas as pd


def load_dataset(file_path):

    # Load dataset
    df = pd.read_csv(file_path)

    print("\nDataset Loaded Successfully\n")

    print(df.head())

    return df


def preprocess_data(df):

    print("\nInitial Dataset Shape:", df.shape)

    # Remove duplicate rows
    df = df.drop_duplicates()

    print("\nDuplicates Removed Successfully")

    # Display missing values before cleaning
    print("\nMissing Values Before Cleaning:\n")

    print(df.isnull().sum())

    # Fill missing numerical values with mean
    numeric_columns = df.select_dtypes(
        include=['int64', 'float64']
    ).columns

    df[numeric_columns] = df[numeric_columns].fillna(
        df[numeric_columns].mean()
    )

    # Convert timestamp column to datetime
    if 'timestamp' in df.columns:

        df['timestamp'] = pd.to_datetime(
            df['timestamp'],
            errors='coerce'
        )

    # Display missing values after cleaning
    print("\nMissing Values After Cleaning:\n")

    print(df.isnull().sum())

    print("\nFinal Dataset Shape:", df.shape)

    return df


def save_processed_data(df, output_path):

    # Save cleaned dataset
    df.to_csv(output_path, index=False)

    print("\nCleaned dataset saved successfully.")

    print(f"\nSaved File Path: {output_path}")


if __name__ == "__main__":

    # Input raw dataset path
    input_path = (
        'data/raw_data/dynamic_supply_chain_logistics_dataset.csv'
    )

    # Output cleaned dataset path
    output_path = (
        'data/processed_data/cleaned_supply_chain.csv'
    )

    # Load dataset
    df = load_dataset(input_path)

    # Preprocess dataset
    df = preprocess_data(df)

    # Save cleaned dataset
    save_processed_data(df, output_path)

    print("\nData preprocessing completed successfully.")