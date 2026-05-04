def create_features(df):
    df['lag_1'] = df['Sales'].shift(1)
    df['lag_7'] = df['Sales'].shift(7)
    df['rolling_mean_7'] = df['Sales'].rolling(7).mean()

    df['day'] = df.index.day
    df['month'] = df.index.month
    df['weekday'] = df.index.weekday

    df = df.dropna()
    return df
