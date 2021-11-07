
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponseRedirect
from django import forms
from .models import *
from django.views import View
# Create your views here.


def test(request):

   return render(request,'QuizApp/quiz.htm',{'bro':'code'})



def home(request):
       


       questions=Question.objects.all()
       request.session.setdefault('created','')
       
   #  #SESSION COUNT(PAGE VISITS FOR ORIGINAL USER)
   #     check=request.session.get('check',0)
   #     count=check+1
   #     request.session['check']=count
         
   #  #TAKING ANSWERS FROM COOKIE INTO SESSION
   #     take3=request.session['name']=request.COOKIES.get('name','none')
   #     take=request.session['id1']=request.COOKIES.get('id1','none')
   #     take2=request.session['id2']=request.COOKIES.get('id2','none')
   
    #Checking if user has submitted quiz/data before
   #  if request.method=="POST":
   #  if take and take2 != 'none':
              
      #  obj1=QuizUserModel.objects.latest('id')  
      #  print(obj1.id)
      #  print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")    
      #  visitor=request.session['visitor']=obj1.id+1
      #  print(f"Heyyyyyyyyyyyyyy {visitor}")
      #  md=QuizUserModel(name=take3,q1=take,q2=take2,unique=visitor)
        
      #  md.save()  
      
      #  obj=QuizUserModel.objects.latest('id')      
   #     print(f"vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv     {obj}")
   #     return render(request,'QuizApp/home.htm',{'show':'no','visit':obj})
   # #  else:
   #      if request.session['check']>=2:
   #          return render(request,'QuizApp/home.htm',{'show':'no','take':take,'take2':take2})
   #      else:
            
       return render(request,'QuizApp/home.htm',{'quest':questions})


        

def questions(request,my_id):
        
        if request.method=="POST":

           arrive=request.session['arrive']='visit'
           score=request.session['score']=request.COOKIES.get('score','none')
           name=request.session['friendname']=request.COOKIES.get('friendname','none')
           
           got_it=QuizFriendModel(name=name,score=score,unique=my_id)
           got_it.save()
          
          
          #one to many relationship to locate friends using that link
           
           obj=QuizFriendModel.objects.filter(unique=my_id)
           return render(request,'QuizApp/quiz.htm',{'obj1':obj,'show':'no'})
        else:
         #IF request is get, show quiz
         take=QuizUserModel.objects.get(pk=my_id)  
         return render(request,'QuizApp/quiz.htm',{'obj':take})



def quest(request):

   id=request.GET['quest']
   quest=id.split("_")
   print(f"###########{quest}#############")
   
   unique=request.COOKIES['sessionid']
   QuizUserModel(name=request.session['name'],unique=unique,category=quest[0],quest_id=quest[1]).save()
   data={
   'category':quest[0],
   'id':quest[1]
   }
   
   return JsonResponse(data)

   
def sessions(request):
   name=request.GET['quest']
   request.session['name']=name
   print(request.session['name'])
   data={
      'done':'done'
   }
   return JsonResponse(data)

