from rest_framework import generics, views, status
from rest_framework.response import Response
from .models import Course, Quiz, Question
from .serializers import CourseSerializer, QuizSerializer, QuestionSerializer, AnswerSerializer

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


"""
[
    {
        "question_id": 1,
        "answer": "a"
    },
    {
        "question_id": 2,
        "answer": "b"
    },
    {
        "question_id": 3,
        "answer": "c"
    }
]
"""

class SubmitAnswers(views.APIView):
    def post(self, request, quiz_id):
        total_score = 0
        serializer = AnswerSerializer(data=request.data, many=True)
        if serializer.is_valid():
            for answer in serializer.validated_data:
                question = Question.objects.get(id=answer['question_id'])
                if answer['answer'] == 'a':
                    total_score += question.score_a
                elif answer['answer'] == 'b':
                    total_score += question.score_b
                elif answer['answer'] == 'c':
                    total_score += question.score_c
                elif answer['answer'] == 'd':
                    total_score += question.score_d
            return Response({'total_score': total_score}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
