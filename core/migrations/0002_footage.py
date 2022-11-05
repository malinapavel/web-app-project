# Generated by Django 4.1.2 on 2022-11-05 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='footages')),
                ('description', models.TextField(max_length=500)),
                ('user', models.CharField(max_length=100)),
                ('sent_on', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
