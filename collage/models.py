from django.db import models
from django.contrib.auth.models import User

class Collage(models.Model):
    cid=models.AutoField
    Firstname=models.CharField(max_length=50, default='')
    Lastname = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    mob = models.CharField(max_length=12, default='')
    add = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=50, default='')
    img = models.ImageField(upload_to="collage/images", default='')
    status = models.CharField(max_length=50, default='no')


    def __str__(self):
        return str(self.Firstname)


