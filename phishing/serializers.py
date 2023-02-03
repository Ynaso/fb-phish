from rest_framework import serializers
from .models import credentials

class CredentialsCapturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = credentials
        fields = ('email', 'password')
