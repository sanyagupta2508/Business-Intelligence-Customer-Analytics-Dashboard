import streamlit as st
import pandas as pd
import os

# 1. Page Config
st.set_page_config(page_title="Retail BI Dashboard", layout="wide")

# Use the "Raw" string path that worked for you
file_path = r'C:\Users\sanya\OneDrive\Desktop\Projects\2. Business Intelligence\Data\cleaned_transactions.csv'
image_folder = r'C:\Users\sanya\OneDrive\Desktop\Projects\2. Business Intelligence\Images'

st.title("Retail Business Intelligence Dashboard")
st.markdown("---")

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    
    # 2. Sidebar Filters
    st.sidebar.header("Filter Analytics")
    all_countries = sorted(df['Country'].unique())
    selected_countries = st.sidebar.multiselect("Select Countries", all_countries, default=[all_countries[0]])
    
    # Filter the data
    filtered_df = df[df['Country'].isin(selected_countries)]

    # 3. Top Row: KPI Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", f"${filtered_df['Total_Sales'].sum():,.2f}")
    col2.metric("Total Orders", filtered_df['TransactionNo'].nunique())
    col3.metric("Avg Order Value", f"${filtered_df['Total_Sales'].mean():,.2f}")
    col4.metric("Unique Customers", filtered_df['CustomerNo'].nunique())

    st.markdown("---")

    # 4. Middle Row: Visualizations from your Images folder
    st.subheader("Sales & Regional Trends")
    tab1, tab2, tab3 = st.tabs(["Monthly Trends", "Top Countries", "Customer Segments"])
    
    with tab1:
        st.image(os.path.join(image_folder, 'monthly_sales_trend.png'), caption="Revenue over time")
    
    with tab2:
        st.image(os.path.join(image_folder, 'top_10_countries.png'), caption="Revenue by Geography")
        
    with tab3:
        st.image(os.path.join(image_folder, 'customer_segments.png'), caption="AI-Powered Customer Groups")

    # 5. Bottom Row: Data Explorer
    st.subheader("🔍 Deep Dive: Transaction Data")
    st.dataframe(filtered_df.head(100), use_container_width=True)

else:
    st.error("Cannot find the cleaned data file. Check the path in app.py!")