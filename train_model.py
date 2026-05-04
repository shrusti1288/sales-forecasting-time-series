from preprocessing import load_data
from feature_engineering import create_features
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

df = load_data("data/sales_data.csv")
df = create_features(df)

features = ['lag_1', 'lag_7', 'rolling_mean_7', 'Promo', 'Holiday', 'day', 'month', 'weekday']

train = df[:-3]
test = df[-3:]

X_train = train[features]
y_train = train['Sales']
X_test = test[features]

model = RandomForestRegressor()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

output = pd.DataFrame({
    'Date': test.index,
    'Actual': test['Sales'],
    'Predicted': predictions
})

output.to_csv("outputs/forecast.csv", index=False)
print(output)
