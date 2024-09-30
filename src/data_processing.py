import pandas as pd

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean the dataset (handle missing values, correct data types)."""
    # Convert InvoiceDate to datetime format
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    # Fill missing values if any (e.g., Purchase_Amount)
    df.fillna(0, inplace=True)
    return df
