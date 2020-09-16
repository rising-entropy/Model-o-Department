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

class DiscreteMath(models.Model):
    id = models.Field(primary_key = True)
    rollNo = models.PositiveIntegerField
    grade = models.CharField(max_length=2)

class DataCommunication(models.Model):
    id = models.Field(primary_key = True)
    rollNo = models.PositiveIntegerField
    grade = models.CharField(max_length=2)

class ComputerOrganisationArchitecture(models.Model):
    id = models.Field(primary_key = True)
    rollNo = models.PositiveIntegerField
    grade = models.CharField(max_length=2)

class SoftwareEngineering(models.Model):
    id = models.Field(primary_key = True)
    rollNo = models.PositiveIntegerField
    grade = models.CharField(max_length=2)

class ProbabilityAndStatistics(models.Model):
    id = models.Field(primary_key = True)
    rollNo = models.PositiveIntegerField
    grade = models.CharField(max_length=2)

class DataStructures(models.Model):
    id = models.Field(primary_key = True)
    rollNo = models.PositiveIntegerField
    grade = models.CharField(max_length=2)