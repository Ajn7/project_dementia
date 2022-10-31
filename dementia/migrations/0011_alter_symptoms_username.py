# Generated by Django 4.0.3 on 2022-10-29 07:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dementia', '0010_remove_symptoms_username_symptoms_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptoms',
            name='username',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]