# serializers.py

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        refresh = self.get_token(user)
        data['user'] = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            # Include any other user information you want
        }
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        return data