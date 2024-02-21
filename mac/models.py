from django.db import models

# Create your models here.
class info(models.Model):
    f_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    re_password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    batch = models.IntegerField()
