import pandas as pd
from sklearn.cluster import KMeans
import pickle

# STEP 1: Load datasets
rain = pd.read_csv("rainfall2.csv")
temp = pd.read_csv("temperature.csv")
aqi = pd.read_csv("aqi.csv", encoding='latin1')

print("Datasets Loaded ✅")

# STEP 2: Check columns
print("Rain:", rain.columns)
print("Temp:", temp.columns)
print("AQI:", aqi.columns)

# STEP 3: Select columns

# Rainfall
rain = rain[['YEAR', 'ANNUAL']]
rain.rename(columns={'ANNUAL': 'rainfall'}, inplace=True)

# Temperature
temp = temp[['YEAR', 'ANNUAL']]
temp.rename(columns={'ANNUAL': 'temperature'}, inplace=True)

# AQI (adjust if needed)
# convert date
aqi['date'] = pd.to_datetime(aqi['sampling_date'], errors='coerce')

# extract year
aqi['YEAR'] = aqi['date'].dt.year

# use pm2_5 as AQI indicator
aqi['AQI'] = pd.to_numeric(aqi['pm2_5'], errors='coerce')

# keep only needed columns
aqi = aqi[['YEAR', 'AQI']]

# remove nulls
aqi = aqi.dropna()

# group by year (important)
aqi = aqi.groupby('YEAR').mean().reset_index()
aqi.rename(columns={'AQI': 'aqi'}, inplace=True)

# STEP 4: Merge
data = pd.merge(rain, temp, on='YEAR')
data = pd.merge(data, aqi, on='YEAR')

# STEP 5: Clean
data['rainfall'] = pd.to_numeric(data['rainfall'], errors='coerce')
data['temperature'] = pd.to_numeric(data['temperature'], errors='coerce')
data['aqi'] = pd.to_numeric(data['aqi'], errors='coerce')

data = data.dropna()

# STEP 6: Features
X = data[['rainfall', 'temperature', 'aqi']]

# STEP 7: Train model
model = KMeans(n_clusters=3, random_state=42)
model.fit(X)

# STEP 8: Assign clusters
data['risk_cluster'] = model.predict(X)

print(data.head())

# STEP 9: Save model
with open("models/risk_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Risk Model Trained Successfully!")