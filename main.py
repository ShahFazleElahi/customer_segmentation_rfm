from src.data_processing import load_data, clean_data
from src.rfm_calculations import calculate_rfm
from src.segmentation import segment_customers
from src.visualization import plot_rfm_distribution, plot_segment_pie_chart, plot_rfm_heatmap
import pandas as pd

def main():
    # Step 1: Load and clean the dataset
    file_path = 'data/customer_data.csv'
    df = load_data(file_path)
    df = clean_data(df)
    
    # Step 2: Calculate RFM metrics (set a reference date for recency calculation)
    reference_date = pd.Timestamp('2024-09-01')
    rfm_df = calculate_rfm(df, reference_date)
    
    # Step 3: Segment customers based on RFM scores
    rfm_df = segment_customers(rfm_df)
    
    # Step 4: Visualize the results
    plot_rfm_distribution(rfm_df)
    plot_segment_pie_chart(rfm_df)
    plot_rfm_heatmap(rfm_df)

if __name__ == "__main__":
    main()
