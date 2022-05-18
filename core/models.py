from datetime import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
    )

class HealthProfile(models.Model):
    weight = models.FloatField(max_length=3)
    height = models.FloatField(max_length=3)
    healthConditions = models.CharField(max_length=500)

    def __str__(self):
        return self.id

class User(models.Model):

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phoneNumber = PhoneNumberField(null=False, blank=False, unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    profilePicture = models.ImageField()
    creationDateTime = models.DateTimeField(default=datetime.now, blank=True)
    dateOfBirth = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    def __str__(self):
        return self.firstName