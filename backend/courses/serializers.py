# serializers.py
from rest_framework import serializers
from .models import Course, Quiz, Question, QuizResult


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    answer = serializers.ChoiceField(choices=["a", "b", "c", "d"])


class QuizResultSerializer(serializers.ModelSerializer):
    quiz_name = serializers.CharField(source="quiz.name", read_only=True)

    class Meta:
        model = QuizResult
        fields = ["id", "quiz", "quiz_name", "score", "completed_date"]
