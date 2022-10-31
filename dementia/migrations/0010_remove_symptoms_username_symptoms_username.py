# Generated by Django 4.0.3 on 2022-10-29 07:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dementia', '0009_symptoms_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symptoms',
            name='username',
        ),
        migrations.AddField(
            model_name='symptoms',
            name='username',
            field=models.ManyToManyField(related_name='symptoms', to=settings.AUTH_USER_MODEL),
        ),
    ]
