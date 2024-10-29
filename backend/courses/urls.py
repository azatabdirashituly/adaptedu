from django.urls import path
from .views import get_courses, StartQuizView, ListQuizzesView

urlpatterns = [
    path("api/courses/", get_courses, name="get_courses"),
    path('quizzes/', ListQuizzesView.as_view(), name='list_quizzes'),
    path('quizzes/<int:quiz_id>/start/', StartQuizView.as_view(), name='start_quiz'),
]
