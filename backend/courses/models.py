from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="courses/images/", blank=True, null=True)
    description = models.TextField()
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.title
