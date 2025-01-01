import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PredictionHistory
from .serializers import PredictionHistorySerializer
from ml_model.model_utils import load_model, predict_price

class PredictPriceView(APIView):
    def post(self, request):
        data = request.data
        try:
            # Extract input data from the request
            area = float(data['area'])  # Update to match your dataset column
            bedrooms = int(data['bedrooms'])
            bathrooms = int(data['bathrooms'])
        except (KeyError, ValueError):
            return Response({"error": "Invalid input. Ensure numeric values are provided."}, status=status.HTTP_400_BAD_REQUEST)

        # Validate input
        if area <= 0 or bedrooms <= 0 or bathrooms <= 0:
            return Response({"error": "All input values must be positive."}, status=status.HTTP_400_BAD_REQUEST)

        # Load ML model and scaler
        try:
            model, scaler = load_model()
        except FileNotFoundError:
            return Response({"error": "Model or scaler not found. Train the model first."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Make prediction
        features = [area, bedrooms, bathrooms]
        predicted_price = predict_price(model, scaler, features)

        # Save the prediction to history
        PredictionHistory.objects.create(
            area=area, bedrooms=bedrooms, bathrooms=bathrooms, predicted_price=predicted_price
        )

        # Return the prediction result
        return Response({"predicted_price": round(predicted_price, 2)}, status=status.HTTP_200_OK)

class PredictionHistoryView(APIView):
    def get(self, request):
        # Fetch all prediction history records
        history = PredictionHistory.objects.all()
        serializer = PredictionHistorySerializer(history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
