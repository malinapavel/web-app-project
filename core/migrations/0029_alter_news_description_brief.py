# Generated by Django 4.1.2 on 2022-11-23 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_footage_pending_req'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description_brief',
            field=models.CharField(max_length=400),
        ),
    ]