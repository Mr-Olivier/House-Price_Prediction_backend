import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
data = pd.read_csv('datasets/raw/house_prices.csv')
X = data[['square_footage', 'bedrooms', 'bathrooms']]
y = data['price']

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
