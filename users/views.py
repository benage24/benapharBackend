from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from.models import User
from rest_framework import generics

from .serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
