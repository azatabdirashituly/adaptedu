from django.contrib import admin
from .models import Course, Quiz, Question

class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

class QuizAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "quiz")

admin.site.register(Course, CourseAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)

# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ("title", "description", "duration")

