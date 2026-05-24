import pandas as pd


def feature_engineering(df):

    # Delay Ratio
    df['delay_ratio'] = (
        df['eta_variation_hours'] /
        (df['lead_time_days'] + 1)
    )

    # Inventory Risk
    df['inventory_risk'] = df[
        'warehouse_inventory_level'
    ].apply(
        lambda x: 1 if x < 100 else 0
    )

    # Temperature Risk
    df['temperature_risk'] = df[
        'iot_temperature'
    ].apply(
        lambda x: 1 if x > 8 else 0
    )

    # Operational Risk Score
    df['operational_risk_score'] = (
        df['traffic_congestion_level'] +
        df['port_congestion_level'] +
        df['route_risk_level']
    )

    # Driver Risk
    df['driver_risk'] = (
        (1 - df['driver_behavior_score']) +
        (1 - df['fatigue_monitoring_score'])
    )

    return df


if __name__ == "__main__":

    # Load processed dataset
    df = pd.read_csv(
        'data/processed_data/processed_supply_chain.csv'
    )

    # Perform feature engineering
    df = feature_engineering(df)

    # Save updated dataset
    df.to_csv(
        'data/processed_data/featured_supply_chain.csv',
        index=False
    )

    print("\nFeature engineering completed successfully.")
    print(df.head())