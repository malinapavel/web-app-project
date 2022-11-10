from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import NewsletterSubscribers, Footage, News
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    allnews = News.objects.all()  
    if request.method == 'POST':
        if 'email-sub' in request.POST:
            email = request.POST['email-sub']
            if '@' in email:
                if NewsletterSubscribers.objects.filter(email = email).exists():
                    messages.info(request, 'You already subscribed to the newsletter.', extra_tags='email')
                
                else: 
                    messages.info(request, 'Thank you, we are glad that you enjoy WeirdoWorld!💗', extra_tags='email')
                    NewsletterSubscribers.objects.create(email=email)
            return render(request, 'index.html', {'display_news' : allnews})

        elif 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return render(request, 'index.html', {'display_news' : allnews})
            else:
                messages.info(request, 'ffffff', extra_tags='login')
                return render(request, 'index.html', {'display_news' : allnews})

    else: 
        return render(request, 'index.html', {'display_news' : allnews})




def index2(request):
    allnews = News.objects.all()  
    return render(request, 'index.html',{'display_news' : allnews})



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
            return render(request, 'contact.html')

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

    return render(request, 'contact.html')


def upload(request):
    if request.method == 'POST':
        if 'myfile' in request.FILES or 'txt' in request.POST:
                user = request.user.username
                img = request.FILES['myfile']
                fss = FileSystemStorage()
                file = fss.save(img.name, img)
                file_url = fss.url(file)
                description = request.POST['txt']

                if user != "":
                    Footage.objects.create(user=user, img=file_url, description=description)
                    return render(request, 'contact.html', {'file_url': file_url})
                else:
                    messages.info(request, 'Sorry, but you need an account to send us footage. 😭', extra_tags='footage')
                    return render(request, 'contact.html')
        else: 
            return render(request, 'contact.html')

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
        
        elif 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return render(request, 'sign-up.html')
            else:
                messages.info(request, 'ffffff', extra_tags='login')
                return render(request, 'sign-up.html')


    else:
        return render(request, 'sign-up.html')



def log_out(request):
    auth.logout(request)
    allnews = News.objects.all()
    return render(request, 'index.html',{'display_news' : allnews})


def all_news(request):
    allnews = News.objects.all().order_by('title')
    if request.method == 'POST':
        if 'email-sub' in request.POST:
            email = request.POST['email-sub']
            if '@' in email:
                if NewsletterSubscribers.objects.filter(email = email).exists():
                    messages.info(request, 'You already subscribed to the newsletter.', extra_tags='email')
                
                else: 
                    messages.info(request, 'Thank you, we are glad that you enjoy WeirdoWorld!💗', extra_tags='email')
                    NewsletterSubscribers.objects.create(email=email)
            return render(request, 'all-news.html', {'display_news' : allnews})

        elif 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return render(request, 'all-news.html', {'display_news' : allnews})
            else:
                messages.info(request, 'ffffff', extra_tags='login')
                return render(request, 'all-news.html', {'display_news' : allnews})
        elif 'search' in request.POST:
            search = request.POST['search']
            keyword_news = []
            for n in allnews:
                if search in n.title:
                    keyword_news.append(n)
            if len(keyword_news) == 0:
                msg_str = 'Sorry, but there are no news containing the keyword "' + search + '".'
                messages.info(request, msg_str, extra_tags='search')
                return render(request, 'all-news.html', {'display_news' : keyword_news})
            else:
                return render(request, 'all-news.html', {'display_news' : keyword_news})
        else:
            return render(request, 'all-news.html', {'display_news' : allnews})
        
    if request.method == 'GET':
        if 'latest' in request.GET:
            latest = request.GET.get('latest')
            sort_date_news = News.objects.all().order_by('written_on') 
            return render(request, 'all-news.html', {'display_news' : sort_date_news})
        elif 'popular' in request.GET:
            popular = request.GET.get('popular')
            sort_pop_news = News.objects.all().order_by('-access_count') 
            return render(request, 'all-news.html', {'display_news' : sort_pop_news})

    return render(request, 'all-news.html', {'display_news' : allnews})
