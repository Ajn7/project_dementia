# Generated by Django 4.0.3 on 2022-10-27 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dementia', '0006_alter_symptoms_description_alter_symptoms_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symptoms',
            name='created',
        ),
    ]