# Generated by Django 4.0.3 on 2022-10-26 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dementia', '0004_alter_symptoms_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptoms',
            name='description',
            field=models.CharField(max_length=150),
        ),
    ]
