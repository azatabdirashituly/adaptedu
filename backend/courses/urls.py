# urls.py
from django.urls import path
from .views import CourseList, QuizList, StartQuiz, SubmitAnswers, UserQuizResults

urlpatterns = [
    path("courses/", CourseList.as_view(), name="course-list"),
    path("quizzes/", QuizList.as_view(), name="quiz-list"),
    path("quizzes/<int:quiz_id>/start/", StartQuiz.as_view(), name="start-quiz"),
    path(
        "quizzes/<int:quiz_id>/submit/", SubmitAnswers.as_view(), name="submit-answers"
    ),
    path(
        "user/quiz-results/", UserQuizResults.as_view(), name="user-quiz-results"
    ),  # New endpoint
]
