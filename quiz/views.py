
from rest_framework.generics import ListAPIView
from .models import Quizzes
from .quizSerializer import QuizSerializer

# Create your views here.
class Quiz(ListAPIView):

    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer
   
