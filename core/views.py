from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import NewsletterSubscribers, Footage

# Create your views here.
def index(request):
    if request.method == 'POST':
        if 'email-sub' in request.POST:
            email = request.POST['email-sub']
            if '@' in email:
                if NewsletterSubscribers.objects.filter(email = email).exists():
                    messages.info(request, 'You already subscribed to the newsletter.', extra_tags='email')
                
                else: 
                    messages.info(request, 'Thank you, we are glad that you enjoy WeirdoWorld!💗', extra_tags='email')
                    NewsletterSubscribers.objects.create(email=email)
            return render(request, 'index.html')

        elif 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return render(request, 'index.html')
            else:
                messages.info(request, 'ffffff', extra_tags='login')
                return render(request, 'index.html')

    else: 
        return render(request, 'index.html')




def index2(request):
    return render(request, 'index.html')

def about_us(request):
    if request.method == 'POST':
        if 'email-sub' in request.POST:
            email = request.POST['email-sub']
            if '@' in email:
                if NewsletterSubscribers.objects.filter(email = email).exists():
                    messages.info(request, 'You already subscribed to the newsletter.', extra_tags='email')
                
                else: 
                    messages.info(request, 'Thank you, we are glad that you enjoy WeirdoWorld!💗', extra_tags='email')
                    NewsletterSubscribers.objects.create(email=email)
            return render(request, 'about-us.html')

        elif 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return render(request, 'about-us.html')
            else:
                messages.info(request, 'ffffff', extra_tags='login')
                return render(request, 'about-us.html')

    else:
        return render(request, 'about-us.html')

def contact(request):

    if request.method == 'POST':
        if 'email-sub' in request.POST:
            email = request.POST['email-sub']
            if '@' in email:
                if NewsletterSubscribers.objects.filter(email = email).exists():
                    messages.info(request, 'You already subscribed to the newsletter.', extra_tags='email')
                
                else: 
                    messages.info(request, 'Thank you, we are glad that you enjoy WeirdoWorld!💗', extra_tags='email')
                    NewsletterSubscribers.objects.create(email=email)
            return render(request, 'conact.html')

        elif 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return render(request, 'contact.html')
            else:
                messages.info(request, 'ffffff', extra_tags='login')
                return render(request, 'contact.html')
        
        #elif 'images' in request.POST:

    return render(request, 'contact.html')

def sign_up(request):
    if request.method == 'POST':
        if 'email-sub' in request.POST:
            email = request.POST['email-sub']
            if '@' in email:
                if NewsletterSubscribers.objects.filter(email = email).exists():
                    messages.info(request, 'You already subscribed to the newsletter.', extra_tags='email')
        
                else: 
                    messages.info(request, 'Thank you, we are glad that you enjoy WeirdoWorld!💗', extra_tags='email')
                    NewsletterSubscribers.objects.create(email=email)
            return render(request, 'sign-up.html')
                    
        elif 'firstname' in request.POST and 'lastname' in request.POST and 'usernamee' in request.POST and 'password' in request.POST and 'confirm_password' in request.POST:  
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            username = request.POST['usernamee']
            password = request.POST['password']
            cpassword = request.POST['confirm_password']


            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Sorry, but this username already exists. 😭', extra_tags='register')
                    return render(request, 'sign-up.html')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, password=password)
                    user.save()
                    messages.info(request, 'Account created successfully! 😃 Please try now to log-in.', extra_tags='register')
                    return render(request, 'sign-up.html')
            else:
                messages.info(request, 'Sorry, but the passwords do not match. 😭', extra_tags='register')
                return render(request, 'sign-up.html')

            return render(request, 'sign-up.html')

        #elif (...): pass

    else:
        return render(request, 'sign-up.html')



def log_out(request):
    auth.logout(request)
    return render(request, 'index.html')


def all_news(request):

    if request.method == 'POST':
        if 'email-sub' in request.POST:
            email = request.POST['email-sub']
            if '@' in email:
                if NewsletterSubscribers.objects.filter(email = email).exists():
                    messages.info(request, 'You already subscribed to the newsletter.', extra_tags='email')
                
                else: 
                    messages.info(request, 'Thank you, we are glad that you enjoy WeirdoWorld!💗', extra_tags='email')
                    NewsletterSubscribers.objects.create(email=email)
            return render(request, 'all-news.html')

        elif 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return render(request, 'all-news.html')
            else:
                messages.info(request, 'ffffff', extra_tags='login')
                return render(request, 'all-news.html')

    return render(request, 'all-news.html')
