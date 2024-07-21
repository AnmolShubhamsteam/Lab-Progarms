from django.db import models

class Course(models.Model):
    cname=models.CharField(max_length=122)
    credits=models.IntegerField()
    def __str__(self) -> str:
        return f"{self.cname}"

class Student(models.Model):
    name=models.CharField(max_length=122)
    usn=models.IntegerField()
    enrollment=models.ManyToManyField(Course)
    def __str__(self) -> str:
        return f"{self.name} | ({self.usn})"
