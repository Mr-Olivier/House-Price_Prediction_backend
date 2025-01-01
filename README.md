🏠 House Price Prediction System Backend

📋 Project Overview
The House Price Prediction System Backend is a Django-powered application that provides machine learning-based predictions for house prices. It includes:

RESTful APIs for predictions and retrieving prediction history.
A trained Linear Regression model to predict house prices based on features like area, bedrooms, and bathrooms.
Persistent storage for tracking prediction history.
🌟 Features
🔮 Prediction Endpoint: Accepts house details (area, bedrooms, bathrooms) and returns the predicted price.
🧠 Machine Learning Integration: Uses a pre-trained Linear Regression model.
📊 History Endpoint: Retrieves all past predictions from the database.
📜 Swagger API Documentation: Interactive API docs for seamless integration.
⚙️ Tech Stack
Django: Web framework for the backend.
Django REST Framework (DRF): For building RESTful APIs.
scikit-learn: For machine learning model training and predictions.
pandas and NumPy: For data preprocessing.
SQLite: Default database for development.
📁 Backend Structure
bash
Copy code
backend/
├── price_prediction/ # Main project configuration
│ ├── settings.py # Project settings
│ ├── urls.py # Root URL configuration
│ ├── wsgi.py # WSGI application
│
├── predictor/ # Predictor app
│ ├── migrations/ # Database migrations
│ ├── models.py # Database models
│ ├── serializers.py # Data serialization for APIs
│ ├── views.py # API logic
│ ├── urls.py # App-specific URL configuration
│
├── ml_model/ # Machine learning module
│ ├── train_model.py # Script to train the ML model
│ ├── model_utils.py # Utilities for loading and using the ML model
│ ├── price_model.pkl # Trained ML model
│ ├── scalers/ # Directory for scalers
│ ├── standard_scaler.pkl
│
├── datasets/ # Dataset-related files
│ ├── raw/ # Raw dataset files
│ ├── house_prices.csv
│
├── manage.py # Django management script
└── requirements.txt # Python dependencies
🚀 How to Set Up and Run
Prerequisites
Python 3.10+
pip (Python package manager)
Steps
Clone the Repository

bash
Copy code
git clone https://github.com/your-repo/house-price-prediction-backend.git
cd house-price-prediction-backend
Set Up a Virtual Environment

bash
Copy code
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Prepare the Database

Run migrations to set up the database:
bash
Copy code
python manage.py makemigrations
python manage.py migrate
Train the Model

Train the ML model and save it:
bash
Copy code
python ml_model/train_model.py
Start the Development Server

bash
Copy code
python manage.py runserver
Test the APIs

Use Postman or cURL to test the /predict/ and /history/ endpoints.
🔗 API Endpoints
Prediction Endpoint
URL: /api/predict/
Method: POST
Request Body:
json
Copy code
{
"area": 2500,
"bedrooms": 4,
"bathrooms": 2
}
Response:
json
Copy code
{
"predicted_price": 15000000.0
}
Prediction History Endpoint
URL: /api/history/
Method: GET
Response:
json
Copy code
[
{
"area": 2500,
"bedrooms": 4,
"bathrooms": 2,
"predicted_price": 15000000.0,
"created_at": "2025-01-01T12:00:00Z"
}
]
🛠️ Training the Machine Learning Model
Dataset:

Ensure the dataset house_prices.csv is placed in datasets/raw/.
Training Script:

Run ml_model/train_model.py to train and save the model:
bash
Copy code
python ml_model/train_model.py
Output Files:

Trained Model: ml_model/price_model.pkl
Scaler: ml_model/scalers/standard_scaler.pkl
📝 Future Enhancements
🌍 Add Location Feature: Incorporate geospatial data for better predictions.
🔒 User Authentication: Secure access to prediction history.
📦 Export Functionality: Allow users to download prediction history.
📈 Batch Predictions: Enable bulk predictions via file upload.
