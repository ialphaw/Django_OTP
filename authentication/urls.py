from django.urls import path
from . import views


app_name = 'authentication'
urlpatterns = [
    path('auth-driver/', views.auth_driver),
]