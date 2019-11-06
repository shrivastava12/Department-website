from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class question(models.Model):
  name = models.CharField(max_length=100)
  emailid = models.EmailField(max_length=100)
  subject = models.CharField(max_length=100)
  answer = models.TextField(max_length=1000)

  def __str__(self):
    return self.name


class Events(models.Model):
  description = models.CharField(max_length=100,blank=True)
  document = models.FileField(upload_to='documents')

  def __str__(self):
    return self.description



class notice(models.Model):
  reason = models.CharField(max_length=200)
  pdf = models.FileField(upload_to='documents')
    
  def __str__(self):
    return self.reason


class profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  fathers_name = models.CharField(max_length=100)
  mothers_name = models.CharField(max_length=100)
  roll_number = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  mobile_no= models.CharField(max_length=10)
  image = models.ImageField(default='default.jpg',upload_to='profile_pics')


  def __str__(self):
    return f'{self.user.username} profile'