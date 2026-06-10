from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# LOAD ALL MODELS (from models folder)
premium_model = pickle.load(open("models/premium_model.pkl", "rb"))
fraud_model = pickle.load(open("models/fraud_model.pkl", "rb"))
risk_model = pickle.load(open("models/risk_model.pkl", "rb"))

# HOME
@app.get("/")
def home():
    return {"message": "GigShield ML API running 🚀"}

# =========================
# PREMIUM API
# =========================
@app.post("/predict")
def predict(data: dict):
    temp = data["temperature"]
    rain = data["rainfall"]
    humidity = data["humidity"]

    risk_score = rain * 0.5 + temp * 0.3 + humidity * 0.2

    features = np.array([[temp, rain, humidity, risk_score]])
    prediction = premium_model.predict(features)

    return {"premium": float(prediction[0])}

# =========================
# FRAUD API
# =========================
@app.post("/fraud")
def detect_fraud(data: dict):
    values = list(data.values())

    prediction = fraud_model.predict([values])

    return {
        "result": "Fraud ❌" if prediction[0] == -1 else "Safe ✅"
    }

# =========================
# RISK API (NEW 🔥)
# =========================
@app.post("/risk")
def detect_risk(data: dict):
    rainfall = data["rainfall"]
    temperature = data["temperature"]
    aqi = data["aqi"]

    features = np.array([[rainfall, temperature, aqi]])
    cluster = risk_model.predict(features)[0]

    if cluster == 0:
        level = "Low"
    elif cluster == 1:
        level = "Medium"
    else:
        level = "High"

    return {"risk": level}