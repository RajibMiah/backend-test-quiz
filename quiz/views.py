
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Quizzes , Question
from .quizSerializer import QuestionSerializer, QuizSerializer, RandomQuestionSerializer 
from rest_framework.views import APIView


class Quiz(ListAPIView):

    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer

class RandomQuestions(APIView):

    def get(self , request , format = None,  **kwargs):

        question = Question.objects.filter(quiz__title = kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question , many = True)

        return Response(serializer.data)

class QuizQuestion(APIView):

    def get(self , request , format = None,  **kwargs):

        quiz = Question.objects.filter(quiz__title = kwargs['topic'])
        serializer = QuestionSerializer(quiz , many = True)

        return Response(serializer.data)