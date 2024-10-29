from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="courses/images/", blank=True, null=True)
    description = models.TextField()
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Quiz(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = 'Quizes'


class Question(models.Model):
    text = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, null=True)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    score_a = models.IntegerField(default=0)
    score_b = models.IntegerField(default=0)
    score_c = models.IntegerField(default=0)
    score_d = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'