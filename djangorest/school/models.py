import datetime
import time
from django.db import models



# Create your models here.
class Schools(models.Model):
    grade_choice = (
        (1, 1),
        (2, 2),
        (3, 3),
    )
    name_school = models.CharField(max_length=200, null=False)
    grade = models.IntegerField(default=0, null=False, choices=grade_choice)

    def __str__(self):
        return self.name_school


class Classes(models.Model):
    name_class = models.CharField(max_length=200, null=False)
    grade = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.name_class


class Students(models.Model):
    sex_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    name_student = models.CharField(max_length=200, null=False)
    birth_date = models.DateField('date birth')
    sex = models.CharField(max_length=10, default='Male', choices=sex_choices, null=False)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, null=False)

    def choice_grade(self):
        x = time.localtime()
        a = self.birth_date[0]
        age = x[0] - a
        grade = age - 5
        if grade <= 0:
            return 'null'
        else:
            return grade

    def __str__(self):
        return self.name_student
