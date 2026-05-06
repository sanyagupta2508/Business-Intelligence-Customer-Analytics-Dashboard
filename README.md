# Retail Business Intelligence and Predictive Analytics

A comprehensive data science project that transforms raw retail transaction data into an interactive Business Intelligence dashboard. This project implements the full data lifecycle, including data cleaning, exploratory analysis, and machine learning deployment.

## Project Overview

This application analyzes a dataset of over 500,000 transactions to provide business owners with actionable insights. It features a predictive model for sales forecasting and an AI-driven customer segmentation tool to help tailor marketing strategies.

## Core Features

*   Interactive BI Dashboard: A web-based interface for monitoring key performance indicators such as total revenue, order count, and customer metrics.
*   Sales Forecasting: Implementation of a Linear Regression model to identify and predict monthly sales trends.
*   Customer Segmentation: Use of K-Means Clustering to categorize customers based on purchase frequency and total spend (RFM analysis).
*   Regional Analysis: Geographic breakdown of sales performance across multiple countries.

## Technical Stack

*   Language: Python
*   Data Processing: Pandas, NumPy
*   Machine Learning: Scikit-Learn (Linear Regression, K-Means Clustering, StandardScaler)
*   Visualization: Matplotlib, Seaborn
*   Web Framework: Streamlit

## Project Structure

*   Data/: Contains raw and processed CSV files.
*   Images/: Visualizations and charts exported from the analysis phase.
*   Notebooks/: Jupyter Notebooks containing the initial data cleaning and model training logic.
*   app.py: The main entry point for the Streamlit web application.
*   requirements.txt: List of necessary Python libraries for reproduction.

## Installation and Setup

1. Clone the repository to your local machine.
2. Create a virtual environment:
   python -m venv venv
3. Activate the virtual environment:
   Windows: venv\Scripts\activate
   Mac/Linux: source venv/bin/activate
4. Install the required packages:
   pip install -r requirements.txt
5. Run the application:
   streamlit run app.py

