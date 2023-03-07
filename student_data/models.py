from django.db import models

# Create your models here.


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=20)
    course_name = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)


class Student(models.Model):
    sid = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


# class FX(models.Model):
#     record_id = models.AutoField(primary_key=True)