import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

# load dataset
df = pd.read_csv("creditcard.csv")

print("Dataset Loaded ✅")

# features
X = df.drop("Class", axis=1)

# train model
model = IsolationForest(contamination=0.002)
model.fit(X)

# test
sample = X.iloc[:5]
pred = model.predict(sample)

print("Predictions:", pred)

# save model
with open("fraud_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Fraud Model Trained Successfully!")