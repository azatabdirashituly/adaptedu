from django.urls import path
from .views import get_courses

urlpatterns = [
    path("api/courses/", get_courses, name="get_courses"),
]
