from django.db import models

# Create your models here.


class Person(models.Model):
    Age = models.IntegerField(null=True)
    Sex = models.CharField(max_length=20, null=True)
    Temp = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    Assessment_Date = models.DateField(auto_now_add=True)
    Assessment_Score = models.IntegerField(null=True)
    Result = models.CharField(max_length=20, null=True)
