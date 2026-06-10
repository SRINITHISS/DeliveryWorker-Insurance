import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pickle

# STEP 1: Load datasets
df1 = pd.read_csv("rainfall.csv")
df2 = pd.read_csv("rainfall2.csv")
df3 = pd.read_csv("temperature.csv")
df4 = pd.read_csv("weather.csv")

# STEP 2: Create simplified dataset
print("DF2 Columns:", df2.columns)
print("DF3 Columns:", df3.columns)

# rainfall from df2 (best structured)
rainfall = df2[['YEAR', 'ANNUAL']].copy()
rainfall.rename(columns={'ANNUAL': 'rainfall'}, inplace=True)

# temperature from df3
temperature = df3[['YEAR', 'ANNUAL']].copy()
temperature.rename(columns={'ANNUAL': 'temperature'}, inplace=True)

# merge temperature + rainfall
data = pd.merge(rainfall, temperature, on='YEAR')
# 🔥 FIX: convert to numeric
data['rainfall'] = pd.to_numeric(data['rainfall'], errors='coerce')
data['temperature'] = pd.to_numeric(data['temperature'], errors='coerce')

# remove invalid values
data = data.dropna()

# add humidity (approx since not available)
data['humidity'] = 70

# STEP 3: Clean
data = data.dropna()

# STEP 4: Feature Engineering
data['risk_score'] = (
    data['rainfall'] * 0.5 +
    data['temperature'] * 0.3 +
    data['humidity'] * 0.2
)

# STEP 5: Target
data['premium'] = data['risk_score'] * 0.8

# STEP 6: Train model
X = data[['temperature', 'rainfall', 'humidity', 'risk_score']]
y = data['premium']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = XGBRegressor()
model.fit(X_train, y_train)

# STEP 7: Test
pred = model.predict(X_test)
print("Sample Predictions:", pred[:5])

# STEP 8: Accuracy
mse = mean_squared_error(y_test, pred)
print("MSE:", mse)

# STEP 9: Save model
with open("premium_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ FINAL MODEL TRAINED SUCCESSFULLY!")