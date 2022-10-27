from django.db import models

# Create your models here.
class symptoms(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    details = models.TextField(max_length=300)
    active = models.BooleanField(default=True)
    #created=models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.name
