from .views import RegistrationAPI
from django.urls import path
urlpatterns = [
    path('api/register/', RegistrationAPI.as_view(), name='register')
]
