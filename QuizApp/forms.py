from django import forms
from django.db.models import fields
from django.forms import ModelForm

from .models import QuizModel

class QuizForm(ModelForm):
    
    class meta:
      model=QuizModel
      #first find solution to create a form which can have images
      #as inputs/or give select options images using jquery

        



