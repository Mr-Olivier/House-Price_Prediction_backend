from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ml_model.model_utils import load_model, predict_price

# Temporary in-memory storage for history
history = []

class PredictPriceView(APIView):
    def post(self, request):
        data = request.data
        try:
            area = float(data['area'])
            bedrooms = int(data['bedrooms'])
            bathrooms = int(data['bathrooms'])
        except (KeyError, ValueError):
            return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)

        # Load model and predict
        model, scaler = load_model()
        predicted_price = predict_price(model, scaler, [area, bedrooms, bathrooms])

        # Store in memory
        history.append({"area": area, "bedrooms": bedrooms, "bathrooms": bathrooms, "predicted_price": predicted_price})

        return Response({"predicted_price": round(predicted_price, 2)}, status=status.HTTP_200_OK)

class PredictionHistoryView(APIView):
    def get(self, request):
        return Response(history, status=status.HTTP_200_OK)
