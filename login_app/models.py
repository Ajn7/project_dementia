
from django.db import models

# Create your models here.
class auth_user(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    
def __str__(self):
    return self.name
