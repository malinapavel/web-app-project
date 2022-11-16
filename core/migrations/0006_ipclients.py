# Generated by Django 4.1.2 on 2022-11-15 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPClients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_client', models.TextField(max_length=50)),
                ('id_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.news')),
            ],
        ),
    ]
