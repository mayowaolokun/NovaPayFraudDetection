from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# ======================
# Load trained model
# ======================
model = joblib.load("best_lgb.pkl")

# ======================
# EXACT feature order used during training (20)
# ======================
FEATURES = [
    "ip_risk_score",
    "risk_score_internal",
    "account_age_days",
    "fee",
    "kyc_tier_enhanced",
    "txn_velocity_1h",
    "amount_src",
    "device_trust_score",
    "txn_velocity_24h",
    "amount_usd",
    "exchange_rate_src_to_dest",
    "location_mismatch",
    "dest_currency_USD",
    "corridor_risk",
    "channel_web",
    "channel_mobile",
    "dest_currency_CAD",
    "ip_country_US",
    "dest_currency_MXN",
    "dest_currency_INR",
]

# ======================
# Request Schema
# ======================
class Transaction(BaseModel):
    ip_risk_score: float
    risk_score_internal: float
    account_age_days: float
    fee: float
    kyc_tier_enhanced: int
    txn_velocity_1h: float
    amount_src: float
    device_trust_score: float
    txn_velocity_24h: float
    amount_usd: float
    exchange_rate_src_to_dest: float
    location_mismatch: int
    dest_currency_USD: int
    corridor_risk: float
    channel_web: int
    channel_mobile: int
    dest_currency_CAD: int
    ip_country_US: int
    dest_currency_MXN: int
    dest_currency_INR: int


# ======================
# FastAPI App
# ======================
app = FastAPI(title="NovaPay Fraud Detection API")


@app.get("/")
def read_root():
    return {"status": "API is running"}


@app.post("/predict/")
def predict(transaction: Transaction):
    # Convert input to ordered numpy array
    data_dict = transaction.dict()
    ordered_values = [data_dict[f] for f in FEATURES]
    X = np.array(ordered_values).reshape(1, -1)

    # Prediction
    prediction = int(model.predict(X)[0])
    probability = float(model.predict_proba(X)[0][1])

    return {
        "prediction": prediction,
        "is_fraud": bool(prediction),
        "fraud_probability": round(probability, 4)
    }
