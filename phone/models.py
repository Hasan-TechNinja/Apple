from django.db import models

# Create your models here.
class Phone(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.IntegerField()