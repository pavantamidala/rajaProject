from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tenth(models.Model):
    tenth_sub_name = models.CharField(max_length=40,blank=True)
    tenth_marks = models.CharField(max_length=40, blank=True)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username +" " + self.tenth_sub_name
    

class Inter(models.Model):
    inter_sub_name = models.CharField(max_length=40, blank=True)
    inter_marks = models.CharField(max_length=40, blank=True)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " " + self.inter_sub_name


class Engineering(models.Model):
    engineer_sub_name = models.CharField(max_length=40, blank=True)
    engineer_marks = models.CharField(max_length=40, blank=True)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " " +self.engineer_sub_name

class Personal(models.Model):
    name = models.CharField(max_length=140,blank=True)
    file = models.ImageField(upload_to="photos/" ,default="default")
    user = models.ForeignKey(User,blank=True,on_delete=models.CASCADE)

