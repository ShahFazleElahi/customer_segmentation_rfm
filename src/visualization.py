import matplotlib.pyplot as plt
import seaborn as sns

def plot_rfm_distribution(rfm_df):
    """Plot the distribution of RFM scores."""
    plt.figure(figsize=(10, 6))
    sns.histplot(rfm_df['RFM_Score'], bins=20, kde=False)
    plt.title('Distribution of RFM Scores')
    plt.xlabel('RFM Score')
    plt.ylabel('Number of Customers')
    plt.show()

def plot_segment_pie_chart(rfm_df):
    """Plot a pie chart for customer segments."""
    segment_counts = rfm_df['Customer_Segment'].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(segment_counts, labels=segment_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2'))
    plt.title('Customer Segments')
    plt.show()

def plot_rfm_heatmap(rfm_df):
    """Plot a heatmap of RFM metrics."""
    plt.figure(figsize=(10, 5))
    sns.heatmap(rfm_df[['Recency', 'Frequency', 'Monetary']].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation between RFM Metrics')
    plt.show()
