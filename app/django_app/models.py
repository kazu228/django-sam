from django.db import models
from django.urls import reverse

# Create your models here.
class Sample(models.Model):
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    age = models.IntegerField()

    def get_absolute_url(self):
        
        return reverse('django_app:create')