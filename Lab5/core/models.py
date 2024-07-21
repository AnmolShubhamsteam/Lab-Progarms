from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=122)
    usn=models.IntegerField()
    def __str__(self)->str:
        return f"{self.name} | ({self.usn})"

class Project(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    ptoic=models.CharField(max_length=122)
    pname=models.CharField(max_length=122)
    planguage=models.CharField(max_length=122)
    
    def __str__(self) -> str:
        return f"{self.pname}"


