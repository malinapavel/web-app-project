# Generated by Django 4.1.2 on 2022-11-19 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_comments_pending_req'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='pending_req',
            field=models.BooleanField(default=False),
        ),
    ]