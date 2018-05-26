from django.db import models

# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length=50)
    def __str__(self):
        return self.school_name

class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=35)
    student_dob = models.DateField('Date of Birth')
    def __str__(self):
        return self.student_name

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)
