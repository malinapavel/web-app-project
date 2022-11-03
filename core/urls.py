from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('index', views.index2, name='index2'),
    path('about_us', views.about_us, name='about_us'),
    path('contact', views.contact, name='contact'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('all_news', views.all_news, name='all_news'),
    path('log_out', views.log_out, name='log_out')
]