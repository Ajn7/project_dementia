from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class symptoms(models.Model):
    username=models.ManyToManyField(User,related_name='symptoms')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    details = models.TextField(max_length=300)
    guidlinevideo=models.URLField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title #+" | "+self.username.username(cant do it because of many to many relationships)
    

class questions(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,related_name="questions") 
    description = models.TextField(max_length=200)
    answer = models.TextField(max_length=300,blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.description+" | "+self.username.username
