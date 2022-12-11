
from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.conf import settings
from django.conf.urls.static import static
from django.template.loader import render_to_string

from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required

from .forms import NewUserCreationForm
from .utils import send_email

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

			return redirect('login')
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
		login(request, user)
		return redirect('home')


@login_required
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


def loginpage(request):
    return render(request, 'login.html')
