
from django.shortcuts import render,HttpResponseRedirect
from django import forms
from .models import QuizFriendModel, QuizModel
# Create your views here.

def home(request):
   
    #SESSION COUNT(PAGE VISITS FOR ORIGINAL USER)
    check=request.session.get('check',0)
    count=check+1
    request.session['check']=count
    
    #TAKING ANSWERS FROM COOKIE INTO SESSION
    take3=request.session['name']=request.COOKIES.get('name','none')
    take=request.session['id1']=request.COOKIES.get('id1','none')
    take2=request.session['id2']=request.COOKIES.get('id2','none')
    
    

    #Checking if user has submitted quiz/data before
    if request.method=="POST":
       if take and take2 != 'none':
          
      
        
        obj1=QuizModel.objects.latest('id')  
        print(obj1.id)
        print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")    
        visitor=request.session['visitor']=obj1.id+1
        print(f"Heyyyyyyyyyyyyyy {visitor}")
        md=QuizModel(nm=take3,q1=take,q2=take2,unique=visitor)
        
        md.save()  
      
        obj=QuizModel.objects.latest('id')      
       print(f"vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv     {obj}")
       return render(request,'QuizApp/home.html',{'show':'no','visit':obj})
    else:
        if request.session['check']>=2:
            return render(request,'QuizApp/home.html',{'show':'no','take':take,'take2':take2})
        else:
           
           return render(request,'QuizApp/home.html',{'take':take,'take2':take2})


        

def questions(request,my_id):
        
        if request.method=="POST":

           arrive=request.session['arrive']='visit'
           score=request.session['score']=request.COOKIES.get('score','none')
           name=request.session['friendname']=request.COOKIES.get('friendname','none')
           
           got_it=QuizFriendModel(name=name,score=score,unique=my_id)
           got_it.save()
          
          
          #one to many relationship to locate friends using that link
           
           obj=QuizFriendModel.objects.filter(unique=my_id)
           return render(request,'QuizApp/quiz.html',{'obj1':obj,'show':'no'})
        else:
         #IF request is get, show quiz
         take=QuizModel.objects.get(pk=my_id)  
         return render(request,'QuizApp/quiz.html',{'obj':take})