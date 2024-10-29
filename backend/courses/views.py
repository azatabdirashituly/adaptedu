# views.py
from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Course, Quiz, Question, QuizResult
from .serializers import (
    CourseSerializer,
    QuizSerializer,
    QuestionSerializer,
    AnswerSerializer,
    QuizResultSerializer,
)


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class QuizList(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class StartQuiz(views.APIView):
    def get(self, request, quiz_id):
        questions = Question.objects.filter(quiz_id=quiz_id)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class SubmitAnswers(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, quiz_id):
        total_score = 0
        serializer = AnswerSerializer(data=request.data, many=True)
        if serializer.is_valid():
            for answer in serializer.validated_data:
                question = Question.objects.get(id=answer["question_id"])
                if answer["answer"] == "a":
                    total_score += question.score_a
                elif answer["answer"] == "b":
                    total_score += question.score_b
                elif answer["answer"] == "c":
                    total_score += question.score_c
                elif answer["answer"] == "d":
                    total_score += question.score_d

            # Save the quiz result
            QuizResult.objects.create(
                user=request.user, quiz_id=quiz_id, score=total_score
            )

            return Response({"total_score": total_score}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserQuizResults(generics.ListAPIView):
    serializer_class = QuizResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return QuizResult.objects.filter(user_id=user_id)
