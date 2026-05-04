# Sales Forecasting with Time Series

🔷 Project Overview

This project predicts future sales using advanced time series and machine learning models like ARIMA, Prophet, and Random Forest.

🔷 Problem Statement

Businesses struggle with inventory planning due to inaccurate demand forecasts. This project solves that by predicting future sales trends.

🔷 Dataset

- Source: Kaggle 
- Features: Date, Sales, Promotions, Holidays

🔷 Tech Stack

- Python (Pandas, NumPy, Scikit-learn)
- Statsmodels (ARIMA)
- Prophet
- Matplotlib / Seaborn

🔷 Workflow

1. Data Cleaning
2. Feature Engineering (lag, rolling stats)
3. Model Building (ARIMA, ML)
4. Evaluation (MAE, RMSE)
5. Visualization

🔷 Results

- Achieved accurate forecasts with low RMSE
- Identified seasonal trends and peak sales periods

🔷 Key Insights

- Sales increase during promotions and weekends
- Strong seasonal patterns observed

🔷 Future Improvements

- LSTM deep learning model
- Real-time forecasting dashboard
- External data integration (weather, events)

🔷 How to Run

pip install -r requirements.txt
python src/train_model.py

🔷 Author

Shrusti Shivalochanamath 

🔷 Linkdin Profile
(https://www.linkedin.com/in/shrusti-shivalochanamath-055464354)

🔷 GitHub Profile
(https://github.com/shrusti1288)

🔷 Recommended Folder Structure

sales-forecasting-time-series/
│
├── data/
│   └── sales_data.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   └── evaluate.py
│
├── outputs/
│   ├── forecasts.csv
│   └── plots.png
│
├── requirements.txt
├── README.md
└── .gitignore

## Overview
Predicts future sales using machine learning.

## How to Run
pip install -r requirements.txt
python src/train_model.py
python src/evaluate.py
