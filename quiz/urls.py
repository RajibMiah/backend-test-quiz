from django.contrib import admin
from django.urls import path
from .views import  Quiz , RandomQuestions ,QuizQuestion

app_name = 'quiz'

urlpatterns = [
    path('', Quiz.as_view() , name ='quiz'),
    path('r/<str:topic>/', RandomQuestions.as_view() , name = 'random'),
    path('q/<str:topic>/', QuizQuestion.as_view() , name = 'all question'),
]
