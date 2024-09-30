def segment_customers(rfm_df):
    """Segment customers based on their RFM scores."""
    def segment(df):
        if df['RFM_Score'] == '555':
            return 'Top Customers'
        elif df['R_rank'] == 1:
            return 'At-Risk Customers'
        elif df['F_rank'] == 5:
            return 'Frequent Customers'
        elif df['M_rank'] == 5:
            return 'High Spend Customers'
        else:
            return 'Others'

    rfm_df['Customer_Segment'] = rfm_df.apply(segment, axis=1)
    return rfm_df
