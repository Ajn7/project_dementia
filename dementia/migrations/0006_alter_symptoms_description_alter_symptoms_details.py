# Generated by Django 4.0.3 on 2022-10-26 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dementia', '0005_alter_symptoms_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptoms',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='symptoms',
            name='details',
            field=models.TextField(max_length=300),
        ),
    ]
