# Generated by Django 4.1.2 on 2022-11-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_comments_pending_req'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='reason',
            field=models.TextField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]