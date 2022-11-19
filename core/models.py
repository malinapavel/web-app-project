from django.db import models
from datetime import datetime

# Create your models here.
class NewsletterSubscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Footage(models.Model):
    img = models.ImageField(upload_to='footages')
    description = models.TextField(max_length = 500)
    user = models.CharField(max_length = 100)
    sent_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user

class News(models.Model):
    img = models.ImageField(upload_to='news')
    title = models.CharField(max_length = 150)
    written_on = models.DateTimeField(default=datetime.now)
    description_brief = models.CharField(max_length = 150)
    description = models.FileField(default='text_articles/dummy.txt')
    access_count = models.IntegerField()
    id = models.IntegerField(primary_key=True)

    def incrementViewCount(self):
        self.access_count += 1
        self.save()


class Comments(models.Model):
    id=models.IntegerField(primary_key=True)
    id_news = models.ForeignKey(News, on_delete=models.CASCADE)
    date_comm = models.DateTimeField(default=datetime.now)
    user = models.CharField(max_length = 100)
    comment = models.TextField(max_length = 500)
    pending_req = models.BooleanField(default=False, editable=True)
    reason_report = models.TextField(max_length = 100, default='.', editable=True)
    
    def __str__(self):
        return self.user
