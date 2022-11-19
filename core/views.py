from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import NewsletterSubscribers, Footage, News, Comments
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from django.shortcuts import get_object_or_404

# Create your views here.

comm_id_list = []

def index(request):
    allnews = News.objects.all() 

    for news in allnews:
        article_txt_brief = ""
        with open(news.description.path,'r') as file:
            tmp = file.readline()

        article_txt_brief = str(tmp[:400] + " . . . . . .")
        news.description_brief = article_txt_brief
        news.save(update_fields=['description_brief'])

    if request.method == 'POST':
        if 'email-sub' in request.POST:
            email = request.POST['email-sub']
            if '@' in email:
                if NewsletterSubscribers.objects.filter(email = email).exists():
                    messages.info(request, 'You have already subscribed to the newsletter.', extra_tags='email')
                
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

    for news in allnews:
        article_txt_brief = ""
        with open(news.description.path,'r') as file:
            tmp = file.readline()

        article_txt_brief = str(tmp[:400] + " . . . . . .")
        news.description_brief = article_txt_brief
        news.save(update_fields=['description_brief'])
        
    return render(request, 'index.html',{'display_news' : allnews})



def about_us(request):
    if request.method == 'POST':
        if 'email-sub' in request.POST:
            email = request.POST['email-sub']
            if '@' in email:
                if NewsletterSubscribers.objects.filter(email = email).exists():
                    messages.info(request, 'You have already subscribed to the newsletter.', extra_tags='email')
                
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
                    messages.info(request, 'You have already subscribed to the newsletter.', extra_tags='email')
                
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
                    if img.size > 1048576*2:
                        messages.info(request, 'Sorry, but the size of the image you just uploaded exceeds 2MB. 😭', extra_tags='footage')
                        return render(request, 'contact.html')
                    else:
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
                    messages.info(request, 'You have already subscribed to the newsletter.', extra_tags='email')
        
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
                    messages.info(request, 'You have already subscribed to the newsletter.', extra_tags='email')
                
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


def news_article(request, id):
    article = News.objects.get(id=id)
    article.access_count += 1
    article.save()
    comment_list = Comments.objects.filter(id_news=article.id).values()

    article_txt = []
    with open(article.description.path,'r') as file:
        tmp = file.readlines()
        for t in tmp:
            if t[-1] == '\n':
                article_txt.append(t)
                article_txt.append("\n")
                

    if request.method == 'POST':
        if 'email-sub' in request.POST:
            email = request.POST['email-sub']
            if '@' in email:
                if NewsletterSubscribers.objects.filter(email = email).exists():
                    messages.info(request, 'You have already subscribed to the newsletter.', extra_tags='email')
                
                else: 
                    messages.info(request, 'Thank you, we are glad that you enjoy WeirdoWorld!💗', extra_tags='email')
                    NewsletterSubscribers.objects.create(email=email)
            return render(request, 'news-article.html', {'news_article' : article, 'comments': comment_list, 'article_txt': article_txt, 'nr_comm': len(comment_list)})

        elif 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return render(request, 'news-article.html', {'news_article' : article, 'comments': comment_list, 'article_txt': article_txt, 'nr_comm': len(comment_list)})
            else:
                messages.info(request, 'ffffff', extra_tags='login')
                return render(request, 'news-article.html', {'news_article' : article, 'comments': comment_list, 'article_txt': article_txt, 'nr_comm': len(comment_list)})
        elif 'comment' in request.POST:
            comment = request.POST['comment']
            username = request.user.username
            if username != "":
                    if comment != "":
                        Comments.objects.create(id_news=article, user=username, comment=comment)
                        return render(request, 'news-article.html', {'news_article' : article, 'comments': comment_list, 'article_txt': article_txt, 'nr_comm': len(comment_list)})
                    else:
                        messages.info(request, 'You cannot send an empty comment.', extra_tags='empty_comm')
                        return render(request, 'news-article.html', {'news_article' : article, 'comments': comment_list, 'article_txt': article_txt, 'nr_comm': len(comment_list)})
            else:
                messages.info(request, 'Sorry, but you need an account to post a comment. 😭', extra_tags='account')
                return render(request, 'news-article.html', {'news_article' : article, 'comments': comment_list, 'article_txt': article_txt, 'nr_comm': len(comment_list)})

    return render(request, 'news-article.html', {'news_article' : article, 'comments': comment_list, 'article_txt': article_txt, 'nr_comm': len(comment_list)})



def report_comm(request):

    comm_id = request.GET.get('comm_id')
    comm_id_list.append(comm_id)
    comm = Comments.objects.filter(id=comm_id).first()

    if request.method == 'POST':
        if 'reasons' in request.POST:
            reason = request.POST['reasons']
            if comm_id_list != 0: comm_id = comm_id_list.pop(0)
            comm = Comments.objects.filter(id=comm_id).first()
            if comm is not None:
                try:
                    comm.pending_req = True
                    comm.reason_report = reason
                    comm.save()
                except AttributeError as e:
                    print("The value assigned to the object is Nonetype")
            if comm_id_list != 0:
                comm_id_list.clear()                    #leave clear for new report
        messages.info(request, "Thank you for your feedback!💗", extra_tags='test')
        return render(request, 'report-form.html', {'comm': comm})
    return render(request, 'report-form.html', {'comm': comm})