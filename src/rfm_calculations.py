import pandas as pd

def calculate_rfm(df, reference_date):
    """Calculate Recency, Frequency, and Monetary (RFM) metrics."""
    # Recency: Days since last purchase
    df['Recency'] = (reference_date - df['InvoiceDate']).dt.days

    # Frequency: Count purchases by each customer
    rfm_df = df.groupby('Customer_ID').agg({
        'Recency': 'min',  # Minimum recency
        'Customer_ID': 'count',  # Total frequency
        'Purchase_Amount': 'sum'  # Total monetary value
    }).rename(columns={'Customer_ID': 'Frequency', 'Purchase_Amount': 'Monetary'})
    
    # Assign RFM scores by quantiles (1 to 5)
    rfm_df['R_rank'] = pd.qcut(rfm_df['Recency'], 5, labels=False) + 1
    rfm_df['F_rank'] = pd.qcut(rfm_df['Frequency'], 5, labels=False) + 1
    rfm_df['M_rank'] = pd.qcut(rfm_df['Monetary'], 5, labels=False) + 1

    # Combine RFM scores into a single RFM score
    rfm_df['RFM_Score'] = rfm_df['R_rank'].astype(str) + rfm_df['F_rank'].astype(str) + rfm_df['M_rank'].astype(str)

    return rfm_df
