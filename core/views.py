from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import NewsletterSubscribers, Footage, News, Comments
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from django.shortcuts import get_object_or_404


# global variable which stores all the ID values of the comments, be it None or an integer
# (stupid implementation, I know, idk better )
comm_id_list = []

# for main page
def index(request):
    allnews = News.objects.all() 

    # open file from the description field and save truncated version in the description_bried field
    # so that it displays a text preview for each article in the main page
    for news in allnews:
        article_txt_brief = ""
        with open(news.description.path,'r') as file:
            tmp = file.readline()

        article_txt_brief = str(tmp[:400] + "...")
        news.description_brief = article_txt_brief
        news.save(update_fields=['description_brief'])

    if request.method == 'POST':
        # check e-mail form
        if 'email-sub' in request.POST:
            email = request.POST['email-sub']
            if '@' in email:
                if NewsletterSubscribers.objects.filter(email = email).exists():
                    messages.info(request, 'You have already subscribed to the newsletter.', extra_tags='email')
                
                else: 
                    messages.info(request, 'Thank you, we are glad that you enjoy WeirdoWorld!💗', extra_tags='email')
                    NewsletterSubscribers.objects.create(email=email)
            return render(request, 'index.html', {'display_news' : allnews})

        # check login form
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



# for main page when you press the "Home" button on the header
def index2(request):
    allnews = News.objects.all()  

    for news in allnews:
        article_txt_brief = ""
        with open(news.description.path,'r') as file:
            tmp = file.readline()

        article_txt_brief = str(tmp[:400] + "...")
        news.description_brief = article_txt_brief
        news.save(update_fields=['description_brief'])
        
    return render(request, 'index.html',{'display_news' : allnews})


# for about us page
def about_us(request):
    if request.method == 'POST':
        # check e-mail form
        if 'email-sub' in request.POST:
            email = request.POST['email-sub']
            if '@' in email:
                if NewsletterSubscribers.objects.filter(email = email).exists():
                    messages.info(request, 'You have already subscribed to the newsletter.', extra_tags='email')
                
                else: 
                    messages.info(request, 'Thank you, we are glad that you enjoy WeirdoWorld!💗', extra_tags='email')
                    NewsletterSubscribers.objects.create(email=email)
            return render(request, 'about-us.html')

        # check login form
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


# for contact page
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


# for the upload section within the contact page
def upload(request):
    if request.method == 'POST':
        # check upload form
        if 'myfile' in request.FILES or 'txt' in request.POST:
                user = request.user.username
                # extract image file path
                img = request.FILES['myfile']          
                # these lines are specifically for the preview part
                fss = FileSystemStorage()
                file = fss.save(img.name, img)
                file_url = fss.url(file)
                description = request.POST['txt']

                # only users can send footage
                if user != "":
                    if img.size > 1048576*2:
                        messages.info(request, 'Sorry, but the size of the image you just uploaded exceeds 2MB. 😭', extra_tags='footage')
                        return render(request, 'contact.html')
                    else:
                        Footage.objects.create(user=user, img=img, description=description)
                        return render(request, 'contact.html', {'file_url': file_url})
                else:
                    messages.info(request, 'Sorry, but you need an account to send us footage. 😭', extra_tags='footage')
                    return render(request, 'contact.html')
        else: 
            return render(request, 'contact.html')

    return render(request, 'contact.html')


# for the registration page
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

        # check register form
        elif 'firstname' in request.POST and 'lastname' in request.POST and 'usernamee' in request.POST and 'password' in request.POST and 'confirm_password' in request.POST:  
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            username = request.POST['usernamee']
            password = request.POST['password']
            cpassword = request.POST['confirm_password']

            # if the password credenditals are correct
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


# logging out
def log_out(request):
    auth.logout(request)
    allnews = News.objects.all()
    return render(request, 'index.html',{'display_news' : allnews})


# for the page which contains all the news
def all_news(request):
    # initially, in the 'all-news' page, all the articles are sorted alphabetically based on their title
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

        # check search form
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
        
    # sorting the news
    if request.method == 'GET':
        if 'latest' in request.GET:
            latest = request.GET.get('latest')
            # sort news from the newest article written (descending)
            sort_date_news = News.objects.all().order_by('-written_on') 
            return render(request, 'all-news.html', {'display_news' : sort_date_news})
        
        elif 'popular' in request.GET:
            popular = request.GET.get('popular')
            # sort news based on the article with the biggest visit count (descending)
            sort_pop_news = News.objects.all().order_by('-access_count') 
            return render(request, 'all-news.html', {'display_news' : sort_pop_news})

    return render(request, 'all-news.html', {'display_news' : allnews})


# for a specific news article
def news_article(request, id):
    article = News.objects.get(id=id)
    # when an article is clicked, increase access count
    article.access_count += 1
    article.save()
    # extract comment chain based on the selected article
    comment_list = Comments.objects.filter(id_news=article.id).values()

    # open file from the description field, so that it displays the whole article text in html
    article_txt = []
    with open(article.description.path,'r') as file:
        tmp = file.readlines()
        for t in tmp:
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
        
        # check comment form
        elif 'comment' in request.POST:
            comment = request.POST['comment']
            username = request.user.username

            # only users can comment
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


# for the report comment form page
def report_comm(request):
    # extract the ID of the selected comment
    comm_id = request.GET.get('comm_id')
    # remember the ID (mentioned this function for two pages, eventually the ID of a comment will be None)
    comm_id_list.append(comm_id)
    comm = Comments.objects.filter(id=comm_id).first()

    if request.method == 'POST':
        # check reasons dropdown form
        if 'reasons' in request.POST:
            reason = request.POST['reasons']
            # pop out any useless value (mostly None values)
            if comm_id_list != 0: 
                comm_id = comm_id_list.pop(0)
            comm = Comments.objects.filter(id=comm_id).first()

            if comm is not None:
                try:
                    comm.pending_req = True
                    comm.reason_report = reason
                    comm.save()
                except AttributeError as e:
                    print("The value assigned to the object is Nonetype")

            #leave clear for new report
            if comm_id_list != 0:
                comm_id_list.clear()                    
        messages.info(request, "Thank you for your feedback!💗", extra_tags='test')
        return render(request, 'report-form.html', {'comm': comm})
    return render(request, 'report-form.html', {'comm': comm})


# for displaying the admin page
def admin_page(request):
    return render(request, 'admin-page.html')


# for the footage table page 
def footage_admin(request):
    # where all the footage ever sent will be displayed on html
    footage = Footage.objects.all()    
    pending_footage = []

    for f in footage:
        # process the footages sent by users
        if f.pending_req == True:
            pending_footage.append(f)

            if request.method == 'POST':
                # check selected elements from the table
                if 'select' in request.POST:
                    select = request.POST.getlist('select')
                    # one or multiple elements were selected, check for each one of them
                    for sel in select:
                        # after doing the old-fashioned way of storing the images and text (copy-paste the text + 'save as' the image)
                        # claim those footages to be solved 
                        #and to never be displayed on the pending request table again (special table created in html, it does not exist in the database)
                        solved_footage = Footage.objects.get(img=sel)
                        solved_footage.pending_req = False
                        solved_footage.save()

                        if f.img == sel:
                            pending_footage.remove(f)
    return render(request, 'footage-admin.html', {'pending_footage': pending_footage, 'nr_pending': len(pending_footage), 'footage': footage})


# for the comments table page
def comm_admin(request):
    # where all the comments ever sent will be displayed on html
    comments = Comments.objects.all()   
    pending_comms = []

    # process the comments flagged as inappropriate
    for c in comments:
        if c.pending_req == True:
            pending_comms.append(c)

    if request.method == 'POST':
        # check selected elements from the table
        if 'select' in request.POST:
            select = request.POST.getlist('select')
            # one or multiple elements were selected, check for each one of them
            for sel in select:
                # claim those comments to be solved and to also be deleted forever from the database
                solved_comms = Comments.objects.get(id=sel)
                solved_comms.pending_req = False
                solved_comms.save()
                pending_comms.remove(solved_comms)
                comments.filter(id=sel).delete()
        return render(request, 'comments-admin.html', {'pending_comms': pending_comms, 'nr_pending': len(pending_comms), 'comments': comments})
    return render(request, 'comments-admin.html', {'pending_comms': pending_comms, 'nr_pending': len(pending_comms), 'comments': comments})


# for the news management page
def news_admin(request):
    # where all the news will be displayed on html
    news = News.objects.all()

    if request.method == 'POST':
        # check news creation form
        if 'ID' in request.POST and 'title' in request.POST and 'myimg' in request.FILES and 'myfile' in request.FILES:
            id = request.POST['ID']
            title = request.POST['title']
            img = request.FILES['myimg']
            description = request.FILES['myfile']
            News.objects.create(id=id, title=title, img=img, description=description, access_count=0)
            return render(request, 'news-admin.html', {'news': news})
    return render(request, 'news-admin.html', {'news': news})