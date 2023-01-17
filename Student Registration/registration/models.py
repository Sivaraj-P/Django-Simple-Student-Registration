from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.IntegerField(primary_key=True)