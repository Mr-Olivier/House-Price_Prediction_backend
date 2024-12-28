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
            sqft = float(data['square_footage'])
            bedrooms = int(data['bedrooms'])
            bathrooms = int(data['bathrooms'])
        except (KeyError, ValueError):
            return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)

        # Load ML model and make prediction
        model, scaler = load_model()
        predicted_price = predict_price(model, scaler, [sqft, bedrooms, bathrooms])

        # Save to history
        PredictionHistory.objects.create(
            square_footage=sqft, bedrooms=bedrooms, bathrooms=bathrooms, predicted_price=predicted_price
        )

        return Response({"predicted_price": predicted_price}, status=status.HTTP_200_OK)

class PredictionHistoryView(APIView):
    def get(self, request):
        history = PredictionHistory.objects.all()
        serializer = PredictionHistorySerializer(history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
