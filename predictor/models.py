from django.db import models

class PredictionHistory(models.Model):
    area = models.FloatField()  # Area (square footage)
    bedrooms = models.IntegerField()  # Number of bedrooms
    bathrooms = models.IntegerField()  # Number of bathrooms
    predicted_price = models.FloatField()  # Predicted price
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"Area: {self.area}, Bedrooms: {self.bedrooms}, Bathrooms: {self.bathrooms}, Price: {self.predicted_price}"
