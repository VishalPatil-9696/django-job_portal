from django.db import models

# Create your models here.
# IT
class jobModel(models.Model):
    Company_Name = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    Package = models.IntegerField()
    Experiance = models.FloatField()
    Opnnings = models.IntegerField()
    Location = models.CharField(max_length=100)
# MECH
class mechJobModel(models.Model):
    Company_Name = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    Package = models.IntegerField()
    Experiance = models.FloatField()
    Opnnings = models.IntegerField()
    Location = models.CharField(max_length=100)
# CIVIL
class civilJobModel(models.Model):
    Company_Name = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    Package = models.IntegerField()
    Experiance = models.FloatField()
    Opnnings = models.IntegerField()
    Location = models.CharField(max_length=100)