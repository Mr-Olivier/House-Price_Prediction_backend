# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('predictor.urls')),
# ]



from django.urls import path, include

urlpatterns = [
    path('api/', include('predictor.urls')),  # Include your app's URLs
]



#   python ml_model/train_model.py
#   python manage.py runserver