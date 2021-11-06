from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here

CHOICES=(
    ('Pow','Power Ranger'),
    ('Ben','Ben 10'),
    
)


class QuizUserModel(models.Model):
    
    name=models.CharField(max_length=100,blank=True)
    unique=models.CharField(max_length=10,default=1)
    quest_id=models.CharField(max_length=10,blank=True)
    category=models.CharField(max_length=10,blank=True)

    
    def __str__(self):
        return str(self.id)




class QuizFriendModel(models.Model):
    unique=models.CharField(default=0,max_length=5)
    name=models.CharField(max_length=10,blank=True)    
    score=models.CharField(max_length=10,blank=True)
    
    def __str__(self):
        return str(self.id)
      
class Question(models.Model):
    picture_1=models.ImageField(upload_to='producting')
    picture_2=models.ImageField(upload_to='producting',default=1)
    picture_3=models.ImageField(upload_to='producting',default=1)
    category=models.CharField(choices=CHOICES,max_length=4) 
    

    def __str__(self):
        return str(self.id)

