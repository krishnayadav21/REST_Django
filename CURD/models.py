from django.db import models

# Create your models here.

class Employee(models.Model):
    Emp_id = models.IntegerField(primary_key=True)
    Emp_Name = models.CharField(max_length=25)
    Salary = models.IntegerField()


def __str__(self):
    return self.Emp_Name
