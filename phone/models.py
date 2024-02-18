from django.db import models

# Create your models here.
class Phone(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.IntegerField()

class Student(models.Model):
    sid = models.IntegerField(max_length = 5)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length= 20)
    clas = models.IntegerField(max_length=5)
    result = models.FloatField(max_length=5)