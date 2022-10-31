from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import NewsletterSubscribers

# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST['email-sub']
        if '@' in email:
            if NewsletterSubscribers.objects.filter(email = email).exists():
                messages.info(request, 'You already subscribed to the newsletter.')
                
            else: 
                messages.info(request, 'Thank you, we are glad that you enjoy WeirdoWorld!💗')
                NewsletterSubscribers.objects.create(email=email)

    return render(request, 'index.html')

def index2(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact.html')

def sign_up(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['usernamee']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Sorry, but this username already exists. 😭')
                return render(request, 'sign-up.html')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, password=password)
                user.save()
                messages.info(request, 'Account created successfully! 😃 Please try now to log-in.')
                return render(request, 'sign-up.html')
        else:
            messages.info(request, 'Sorry, but the passwords do not match. 😭')
            return render(request, 'sign-up.html')

    else:
        return render(request, 'sign-up.html')

def all_news(request):
    return render(request, 'all-news.html')
