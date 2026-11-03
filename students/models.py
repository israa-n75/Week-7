from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Course Model
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name