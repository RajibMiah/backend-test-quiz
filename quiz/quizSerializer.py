from django.db import models
from rest_framework import serializers
from .models import Quizzes , Question , Answer

class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields =['title',]