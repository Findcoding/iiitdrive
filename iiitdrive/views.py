
from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.conf import settings
from django.conf.urls.static import static
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth import get_user_model, login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import NewUserCreationForm
from .utils import send_email
from .models import UserDetails

User = get_user_model()

def indexpage(request):
    print("hello world")
    return render(request, 'index.html')


def signup(request):
	if request.method == 'POST':
		form = NewUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()

			current_site = request.get_host()
			subject = 'Email Verification'

			message = render_to_string(
				'verification_email.html', {
				'username': user.username,
				'domain': current_site,
				'token': user.email_verification_token,
			})
			send_email(subject, user.email, message)

			request.method = 'GET'
			context = {'alert_message' : 'Account Created Successfully, Check Email Inbox for Verification Link'}
			return login(request, **context)
	else:
		form = NewUserCreationForm()
	return render(request, 'registration/signup.html', {'form': form})


def verify_email(request, token) :
	user = User.objects.filter(email_verification_token = token).first()

	if user is None :
		return redirect('home') #bad token, show error or so
	elif user.email_verified :
		return redirect('home') #email already verified
	else :
		user.email_verified = True
		user.is_active = True
		user.save()
		auth_login(request, user)
		return redirect('home')

def login(request, *args, **kwargs):
	context = kwargs

	form = AuthenticationForm()
	context.update({'form' : form})
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user:
			if user.is_active:
				auth_login(request, user)
				return redirect('home')
		else:
			messages.error(request, 'Incorrect Username or Password. Please enter a correct Username and Password.')

	return render(request, 'registration/login.html', context)


@login_required
def homepage(request):
	return render(request, 'home.html')

@login_required
def profile(request):
	user_details = UserDetails.objects.get(user = request.user)
	if request.method == 'POST':
		if 'profile_image' in request.FILES :
			user_details.profile_picture = request.FILES['profile_image']
			user_details.save()
		elif 'about_me' in request.POST :
			user_details.about_me = request.POST['about_me']
			user_details.save()

	return render(request, 'profile.html')

def upload(request):
    return render(request, 'upload.html')


def mydrive(request):
    if request.method == 'POST':
        post_data = request.POST
        print(post_data)

        return render(request, 'mydrive.html')

    return render(request, 'mydrive.html')

def starred(request):
    return render(request, 'starred.html')

def trash(request):
    return render(request, 'trash.html')


def social(request):
    return render(request, 'social.html')



