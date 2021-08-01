
from django.contrib import admin
from .models import QuizFriendModel, QuizModel
# Register your models here.



@admin.register(QuizModel)
class QuizModelAdmin(admin.ModelAdmin):
    list_display=['nm','unique']


@admin.register(QuizFriendModel)
class QuizFriendModelAdmin(admin.ModelAdmin):
    list_display=['name','score']