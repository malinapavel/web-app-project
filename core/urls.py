from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.index, name='index'),
    path('index', views.index2, name='index2'),
    path('about_us', views.about_us, name='about_us'),
    path('contact', views.contact, name='contact'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('all_news', views.all_news, name='all_news'),
    path('log_out', views.log_out, name='log_out'),
    path('upload', views.upload, name='upload'),
    path('<int:id>/', views.news_article, name='news_article'),
    path('report_comm', views.report_comm, name='report_comm'),
    path('admin_page', views.admin_page, name='admin_page'),
    path('footage_admin', views.footage_admin, name='footage_admin'),
    path('comm_admin', views.comm_admin, name='comm_admin'),
    path('news_admin', views.news_admin, name='news_admin')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)