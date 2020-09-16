from django.db import models

# Create your models here.

class Teacher(models.Model):
    id = models.Field(primary_key = True)
    mail = models.EmailField
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)

class Student(models.Model):
    id = models.Field(primary_key = True)
    mail = models.EmailField
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    year = models.PositiveIntegerField
    branch = models.CharField(max_length=50)
    rollNo = models.PositiveIntegerField
    DMgrade = models.CharField(max_length=2, default="NA")
    DCgrade = models.CharField(max_length=2, default="NA")
    COAgrade = models.CharField(max_length=2, default="NA")
    SEgrade = models.CharField(max_length=2, default="NA")
    PaSgrade = models.CharField(max_length=2, default="NA")
    DSgrade = models.CharField(max_length=2, default="NA")
