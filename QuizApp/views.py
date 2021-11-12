
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,HttpResponseRedirect
from django import forms
from .models import *
from django.views import View
from django.db.models import Q




#Render questions to user and create a session
def home(request):
       
       questions=Question.objects.all()
       request.session.setdefault('created','')
            
       return render(request,'QuizApp/home.htm',{'quest':questions})

     

#Render predefined questions to friend and set user's session id in key cookie for reference 
def questions(request,id):

        questions=Question.objects.all()
      
        take= render(request,'QuizApp/questions.htm',{'quest':questions})
        take.set_cookie('key',id,httponly=True)
        
        request.session.setdefault('friend','')
        return take



#Get user ans and category on each answer and save it as database
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


#Set name of user in session after clicking on start button   
def sessions(request):
   name=request.GET['quest']
   request.session['name']=name
         
   data={
      'link':request.COOKIES['sessionid']
   }
   return JsonResponse(data)



#Check question id and category clicked by friend against usermodel(through key set up during question rendring for friend)
def check(request):
       
       id=request.GET['quest']
       quest=id.split("_")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
       keys=QuizUserModel.objects.filter(unique=request.COOKIES['key'])
       print(f"#############{keys}####of friend ############")
       for key in keys:
          print(f"##bbb####{key.quest_id}####{quest[1]}####")
          print(f"###bbb###{key.category}###{quest[0]}###")
          if key.quest_id==quest[1] and key.category==quest[0]:
             
              friend=QuizFriendModel.objects.get(unique=request.COOKIES['sessionid'],user_belong_to=key.unique)
            
              friend.score+=1
              friend.save()
              data={
                'answer':'Correct'
             }
             
              return JsonResponse(data) 
          
          data={
                'answer':'Wrong'
             }    
     
         
       return JsonResponse(data)      




#Provide link for score and set friendname in session 
def quizsessions(request):
   
   name=request.GET['quest']
   request.session['name']=name
   
   QuizFriendModel(unique=request.COOKIES['sessionid'],user_belong_to=request.COOKIES['key'],name=request.session['name']).save()
      
   data={
      'link':request.COOKIES['sessionid']
   }
   return JsonResponse(data)
 

#To show result of author and it's users
def result(request,pk):
    total=0
    user=QuizUserModel.objects.filter(unique=pk).first() 
    #result of all friends of user
    friends=QuizFriendModel.objects.filter(user_belong_to=user.unique)
    
    

    return render(request,'QuizApp/result.htm',{'results':friends,'name':user.name})