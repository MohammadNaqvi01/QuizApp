from django.urls import path,include
from QuizApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home,name="home"),
    path('quiz/<slug:id>',views.questions),
    
    path('userquest/',views.quest),
    path('username/',views.sessions),
    path('check/',views.check),
    path('quizusername/',views.quizsessions),
    path('result/<slug:pk>',views.result),

    
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)