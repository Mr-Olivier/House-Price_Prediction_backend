import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Ensure directories exist
os.makedirs('ml_model/scalers', exist_ok=True)

# Load dataset
data = pd.read_csv('datasets/raw/house_prices.csv')

# Select relevant columns
X = data[['area', 'bedrooms', 'bathrooms']]  # Use columns from your dataset
X.columns = ['square_footage', 'bedrooms', 'bathrooms']  # Rename for consistency
y = data['price']  # Target variable

# Preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model and scaler
joblib.dump(model, 'ml_model/price_model.pkl')
joblib.dump(scaler, 'ml_model/scalers/standard_scaler.pkl')

print("Model and scaler saved successfully!")
