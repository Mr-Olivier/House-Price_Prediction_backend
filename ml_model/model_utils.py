import joblib
import numpy as np

def load_model():
    model = joblib.load('ml_model/price_model.pkl')
    scaler = joblib.load('ml_model/scalers/standard_scaler.pkl')
    return model, scaler

def predict_price(model, scaler, features):
    features = np.array(features).reshape(1, -1)
    scaled_features = scaler.transform(features)
    return model.predict(scaled_features)[0]
