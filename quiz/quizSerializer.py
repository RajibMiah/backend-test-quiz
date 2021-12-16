from django.db import models
from rest_framework import serializers
from .models import Quizzes , Question , Answer

class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quizzes
        fields =['title',]

class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = serializers.StringRelatedField(many = True)
    
    class Meta:
        model = Question
        fields = ['title' , 'answer']