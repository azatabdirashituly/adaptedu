from django.contrib import admin
from .models import Course, Quiz, Question

admin.site.register(Course)
admin.site.register(Quiz)
admin.site.register(Question)

# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ("title", "description", "duration")

