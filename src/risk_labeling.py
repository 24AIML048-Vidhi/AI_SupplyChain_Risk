import pandas as pd


def classify_risk(row):

    # Supplier Risk
    if row['supplier_reliability_score'] < 0.3:
        return 'Supplier Risk'

    # Logistics Risk
    elif (
        row['eta_variation_hours'] > 5 or
        row['traffic_congestion_level'] > 7 or
        row['port_congestion_level'] > 7
    ):
        return 'Logistics Risk'

    # Quality Risk
    elif (
        row['cargo_condition_status'] == 0 or
        row['iot_temperature'] > 8
    ):
        return 'Quality Risk'

    # Demand Risk
    elif (
        row['warehouse_inventory_level'] < 100 or
        row['historical_demand'] > 800
    ):
        return 'Demand Risk'

    # External Disruption Risk
    elif row['weather_condition_severity'] > 0.7:
        return 'External Disruption Risk'

    # Operational Risk
    elif (
        row['handling_equipment_availability'] == 0 or
        row['loading_unloading_time'] > 4
    ):
        return 'Operational Risk'

    # Transportation Risk
    elif (
        row['driver_behavior_score'] < 0.4 or
        row['fatigue_monitoring_score'] < 0.4
    ):
        return 'Transportation Risk'

    else:
        return 'Low Risk'


def calculate_risk_score(row):

    risk_score = (
        row['traffic_congestion_level'] +
        row['port_congestion_level'] +
        row['route_risk_level'] +
        row['eta_variation_hours'] +
        (row['weather_condition_severity'] * 10)
    )

    return risk_score


def classify_severity(score):

    if score < 10:
        return 'Low'

    elif score < 20:
        return 'Medium'

    else:
        return 'High'


def generate_risk_labels(df):

    # Create Risk Classification column
    df['generated_risk_classification'] = df.apply(
        classify_risk,
        axis=1
    )

    # Create Risk Score column
    df['risk_score'] = df.apply(
        calculate_risk_score,
        axis=1
    )

    # Create Severity Level column
    df['severity_level'] = df['risk_score'].apply(
        classify_severity
    )

    return df


# Run file directly
if __name__ == "__main__":

    # Load dataset
    df = pd.read_csv(
        'data/processed_data/cleaned_supply_chain.csv'
    )

    # Generate labels
    df = generate_risk_labels(df)

    # Show output
    print(
        df[
            [
                'generated_risk_classification',
                'risk_score',
                'severity_level'
            ]
        ].head()
    )

    # Save processed dataset
    df.to_csv(
        'data/processed_data/processed_supply_chain.csv',
        index=False
    )

    print("\nRisk labeling completed successfully.")