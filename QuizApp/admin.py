
from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(QuizUserModel)
class QuizUserModelAdmin(admin.ModelAdmin):
    list_display=['id','name','unique','quest_id','category']


@admin.register(QuizFriendModel)
class QuizFriendModelAdmin(admin.ModelAdmin):
    list_display=['id','name','score']


@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display=['id','picture_1','picture_2','picture_3','category']