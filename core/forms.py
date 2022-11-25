from django import forms
from django.forms import ModelForm, EmailInput
from . models import NewsletterSubscribers

class NewsletterSubscribersForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscribers
        fields = ['email', ]
        
