import pandas as pd

def load_data(filepath):
    """Load CSV threat data into a DataFrame."""
    return pd.read_csv(filepath)

def filter_by_severity(df, severity):
    """Filter threats by severity level."""
    return df[df["Severity"] == severity]

def export_to_csv(df, filename="filtered_threats.csv"):
    """Export filtered data to CSV."""
    df.to_csv(filename, index=False)
    return filename
