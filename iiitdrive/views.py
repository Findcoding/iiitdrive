
from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

# Create your views here.


def indexpage(request):
    print("hello world")
    return render(request, 'index.html')


def homepage(request):
    return render(request, 'home.html')

def profile(request):
    if request.method == 'POST':
        # post_data = request.POST.dict()
        post_data = request.POST
        print(post_data)

        return redirect(homepage)

    return render(request, 'profile.html')

def upload(request):
    return render(request, 'upload.html')


def mydrive(request):
    return render(request, 'mydrive.html')

def starred(request):
    return render(request, 'starred.html')

def trash(request):
    return render(request, 'trash.html')


def social(request):
    return render(request, 'social.html')