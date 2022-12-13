
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
from django.db import models

from .forms import NewUserCreationForm
from .utils import send_email
from .models import UserDetails, Social, ResourceFile, UserFiles

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
	if request.method == 'POST':
		post_data = request.POST
		print(post_data)
		return render(request, 'home.html')

	return render(request, 'home.html')

@login_required
def profile(request):
	user_details = UserDetails.objects.get(user = request.user)
	if request.method == 'POST':
		if 'profile_image' in request.FILES :
			user_details.profile_picture = request.FILES['profile_image']
			user_details.save()
		else:
			if 'about_me' in request.POST :
				user_details.about_me = request.POST['about_me']
				user_details.save()
			for social in ['github', 'linkedin', 'twitter', 'instagram', 'facebook', 'reddit'] :
				if social in request.POST :
					if Social.objects.filter(user_details = user_details, name = social).exists() :
						user_social = Social.objects.get(user_details = user_details, name = social)
					else :
						user_social = Social()
						user_social.user_details = user_details
						user_social.name = social
					user_social.link = request.POST[social]
					user_social.save()

	return render(request, 'profile.html')


@login_required
def mydrive(request):
	user = request.user
	files = UserFiles.objects.filter(models.Q(owner=user) & models.Q(is_trashed=False))
	if request.method == 'POST':
		if 'document' in request.FILES :
			for f in request.FILES.getlist('document'):
				r_file = ResourceFile.objects.create(file = f)
				UserFiles.objects.create(owner=user, file=r_file)
		elif 'rename_id' in request.POST and 'rename' in request.POST :
			file = files.filter(file__uid = request.POST['rename_id']).first()
			if file is not None :
				file.file.name = request.POST['rename']
				file.file.save()
		elif 'star_id' in request.POST :
			file = files.filter(file__uid = request.POST['star_id']).first()
			print(file)
			if file is not None :
				file.is_starred = not(file.is_starred)
				file.save()
		# elif 'trash_id' in request.POST :
		# 	file = files.filter(file__uid = request.POST['trash_id']).first()
		# 	print(file)
		# 	if file is not None :
		# 		file.is_trashed = not(file.is_trashed)
		# 		file.save()

	context = {'files' : files}

	return render(request, 'mydrive.html', context)

def starred(request):
	user = request.user
	files = UserFiles.objects.filter(models.Q(owner=user) & models.Q(is_trashed=False))

	context = {'files' : files}

	return render(request, 'starred.html', context)

def trash(request):
    return render(request, 'trash.html')


def social(request):
    return render(request, 'social.html')



