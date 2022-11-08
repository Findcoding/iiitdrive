
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


def upload(request):
    return render(request, 'upload.html')