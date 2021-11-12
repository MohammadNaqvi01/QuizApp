from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here

CHOICES=(
    ('Pow','Power Ranger'),
    ('Ben','Ben 10'),
    
)

#Can also create by explicitily mentioning the category name as modelfield and instead of saving question id
#under quest_id to category but for that i need all the data send to user to evaluate against user model at once 
# as there would be only one user object for all questions
class QuizUserModel(models.Model):
    
    name=models.CharField(max_length=100,blank=True)
    unique=models.CharField(max_length=10,default=1)
    quest_id=models.CharField(max_length=10,blank=True)
    category=models.CharField(max_length=10,blank=True)

    
    def __str__(self):
        return str(self.id)


#Could use foreign key but only when the user it belongs to is also one
#else either need many to many relationship if go by one userobject per question or user many to many or
#the one i m using right now to identify which user this friend belongs to with help of sessions 
#to create a object (user) for all questions i would need to render all questions as a form 
#as i need validation of all at once when there is only one object for all questions
class QuizFriendModel(models.Model):
    user_belong_to=models.CharField(max_length=50)
    name=models.CharField(max_length=10,blank=True)
    unique=models.CharField(max_length=50,blank=True)
  
    score=models.PositiveIntegerField(null=True,default=0)
    
    def __str__(self):
        return str(self.id)
      
class Question(models.Model):
    picture_1=models.ImageField(upload_to='producting')
    picture_2=models.ImageField(upload_to='producting',default=1)
    picture_3=models.ImageField(upload_to='producting',default=1)
    category=models.CharField(choices=CHOICES,max_length=4) 
    

    def __str__(self):
        return str(self.id)

