from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('driver/me/', views.DriverInfo.as_view()),
    path('passenger/me/', views.PassengerInfo.as_view()),
]