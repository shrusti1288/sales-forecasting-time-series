import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

df = pd.read_csv("outputs/forecast.csv")

mae = mean_absolute_error(df['Actual'], df['Predicted'])
rmse = np.sqrt(mean_squared_error(df['Actual'], df['Predicted']))

print("MAE:", mae)
print("RMSE:", rmse)
