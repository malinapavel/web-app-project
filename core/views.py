from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('<p>Hi</p>')
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact.html')

def sign_up(request):
    return render(request, 'sign-up.html')

def all_news(request):
    return render(request, 'all-news.html')
