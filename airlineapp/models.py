from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=128)
    isAdmin = models.BooleanField(default=False)
    milesandsmiles = models.BooleanField(default=False)


class Flight(models.Model):
    flightid = models.IntegerField(primary_key=True)
    starttime = models.DateTimeField()
    finishtime = models.DateTimeField()
    duration = models.FloatField()
    startairport = models.CharField(max_length=100)
    finishairport = models.CharField(max_length=100)
    totalseats = models.IntegerField()
    flightname = models.CharField(max_length=100)