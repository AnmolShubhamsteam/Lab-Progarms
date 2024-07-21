from django.db import models

class Course(models.Model):
    cname=models.CharField(max_length=122)
    ccredit=models.IntegerField()
    def __str__(self) -> str:
        return f"{self.cname} | {self.ccredit}"


class Student(models.Model):
    sname=models.CharField(max_length=122)
    enrollment=models.ManyToManyField(Course)
    def __str__(self):
        return f"{self.sname}"