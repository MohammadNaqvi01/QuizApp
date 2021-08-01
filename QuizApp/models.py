from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here

class QuizModel(models.Model):
    
    nm=models.CharField(max_length=100,blank=True)
    q1=models.CharField(max_length=10,blank=True)
    q2=models.CharField(max_length=10,blank=True)
    unique=models.CharField(max_length=10,default=1)
    
    def __str__(self):
        return str(self.id)

#WRITE ONE TO MANY RELATIONSHIP MODEL

class QuizFriendModel(models.Model):
    unique=models.CharField(default=0,max_length=5)
    name=models.CharField(max_length=10,blank=True)    
    score=models.CharField(max_length=10,blank=True)
    def __str__(self):
        return str(self.id)
      
