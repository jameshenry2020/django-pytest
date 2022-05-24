from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    admission_number = models.IntegerField(unique=True)
    is_qualified = models.BooleanField(default=False)
    grade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name

    def get_grade(self):
        if self.grade < 40:
            return "Fail"
        elif 40 < self.grade < 70:
            return "Passed"
        elif 70 < self.grade < 100:
            return "Excellent"
        else:
            return "Error"


class ClassRoom(models.Model):
    name = models.CharField(max_length=200)
    student_capacity = models.IntegerField()
    students = models.ManyToManyField("Student")

    def __str__(self):
        return self.name
