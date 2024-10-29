from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import Course, Question, Quiz
from .serializers import CourseSerializer, QuestionSerializer, QuizSerializer


@api_view(["GET"])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

class StartQuizView(APIView):
    def get(self, request, quiz_id):
        questions = Question.objects.filter(quiz_id=quiz_id)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

class ListQuizzesView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer



