from django.db import models

# Create your models here.
class Sample(models.Model):
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    age = models.IntegerField(max_length=100)