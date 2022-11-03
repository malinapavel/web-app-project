from django.db import models

# Create your models here.
class NewsletterSubscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Footage(models.Model):
    #img_url = 
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.description
