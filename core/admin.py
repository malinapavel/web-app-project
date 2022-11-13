from django.contrib import admin
from . models import NewsletterSubscribers, Footage, News, Comments

# Register your models here.
admin.site.register(NewsletterSubscribers)
admin.site.register(Footage)
admin.site.register(News)
admin.site.register(Comments)