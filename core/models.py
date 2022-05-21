from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title

SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
    )

class HealthProfile(models.Model):
    weight = models.FloatField(max_length=3)
    height = models.FloatField(max_length=3)
    healthConditions = models.CharField(max_length=500)

    def __str__(self):
        return self.healthConditions

class Address(models.Model):
    houseNumber = models.CharField(max_length=10)
    kebele = models.IntegerField()
    subCity = models.CharField(max_length=50)
    regionOrCity = models.CharField(max_length=50)
    country = models.CharField(max_length=70)

    def __str__(self):
        return self.houseNumber

class Users(models.Model):

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
    healthProfileID = models.ForeignKey(HealthProfile, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    additionalAttributes = models.CharField(max_length=500)

    USERNAME_FIELD = 'username'
    PASSWORD_FIELD = 'password'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.firstName + " " + self.lastName

class Admin(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phoneNumber = PhoneNumberField(null=False, blank=False, unique=True)
    username = models.CharField(null=False, blank=False, unique=True, max_length=50)
    password = models.CharField(max_length=50)
    profilePicture = models.ImageField()
    creationDateTime = models.DateTimeField(default=datetime.now, blank=True)

class HealthFacilityAccount(models.Model):
    healthFacilityOrAmbulanceID = models.ForeignKey('core.AmbulanceService', on_delete=models.CASCADE) #check if this works
    healthFacilityType =  models.CharField(max_length=100)
    username =  models.CharField(max_length=50, unique=True)
    email =  models.CharField(max_length=100)
    password =  models.CharField(max_length=50)
    creationDateTime = models.DateTimeField(default=datetime.now, blank=True)
    logo = models.ImageField()
    additionalAttributes = models.CharField(max_length=500)

class HealthCareFacility(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    address = models.ForeignKey(Admin, on_delete=models.CASCADE)
    averageRating = models.FloatField()
    GPSCoordinates = models.CharField(max_length=100)
    verificationStatus = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneNumber = PhoneNumberField(null=False, blank=False, unique=True)
    source = models.CharField(max_length=100)
    imageGallery = models.ImageField()
    tags = models.CharField(max_length=100)
    accountID = models.ForeignKey(HealthFacilityAccount, on_delete=models.CASCADE)
    creationDateTime = models.DateTimeField(default=datetime.now, blank=True)
    type =  models.CharField(max_length=100)
    services =  models.CharField(max_length=100)
    capacity =  models.CharField(max_length=100)
    doctorCount =  models.IntegerField()
    averageNumberOfUsers = models.FloatField()
    additionalAttributes =  models.CharField(max_length=500)

class Appointment(models.Model):
    userID = models.ForeignKey(Users, on_delete=models.CASCADE)
    healthFacilityID = models.ForeignKey(HealthCareFacility, on_delete=models.CASCADE)
    healthFacilityType = models.CharField(max_length=100)
    dateTime = models.DateTimeField()
    status = models.CharField(max_length=50)

class UserRating(models.Model):
    userID = models.ForeignKey(Users, on_delete=models.CASCADE)
    healthFacilityID = models.ForeignKey(HealthCareFacility, on_delete=models.CASCADE)
    rating = models.IntegerField()
    healthFacilityType = models.CharField(max_length=100)
    creationDateTime = models.DateTimeField(default=datetime.now, blank=True)
    lastUpdateTime = models.DateTimeField(default=datetime.now, blank=True)

class UserReview(models.Model):
    userID = models.ForeignKey(Users, on_delete=models.CASCADE)
    healthFacilityID = models.ForeignKey(HealthCareFacility, on_delete=models.CASCADE)
    review = models.CharField(max_length=200)
    healthFacilityType = models.CharField(max_length=100)
    creationDateTime = models.DateTimeField(default=datetime.now, blank=True)
    lastUpdateTime = models.DateTimeField(default=datetime.now, blank=True)

class ReviewComment(models.Model):
    commenterID = models.ForeignKey(UserRating, on_delete=models.CASCADE)
    UserReviewID = models.ForeignKey(UserReview, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    creationDateTime = models.DateTimeField(default=datetime.now, blank=True)
    lastUpdateTime = models.DateTimeField(default=datetime.now, blank=True)

class AmbulanceService(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    address = models.ForeignKey(Admin, on_delete=models.CASCADE)
    averageRating = models.FloatField()
    GPSCoordinates = models.CharField(max_length=100)
    verificationStatus = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneNumber = PhoneNumberField(null=False, blank=False, unique=True)
    source = models.CharField(max_length=100)
    imageGallery = models.ImageField()
    tags = models.CharField(max_length=100)
    accountID = models.ForeignKey(HealthCareFacility, on_delete=models.CASCADE)
    creationDateTime = models.DateTimeField(default=datetime.now, blank=True)
    additionalAttributes = models.CharField(max_length=500)

class Ambulance(models.Model):
    healthFacilityID = models.ForeignKey(AmbulanceService, on_delete=models.CASCADE)
    healthFacilityType = models.CharField(max_length=100)
    driverFirstName = models.CharField(max_length=100)
    driverLastName = models.CharField(max_length=100)
    isAvailable = models.BooleanField(default=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    phoneNumber = PhoneNumberField(null=False, blank=False, unique=True)
    accountID = models.ForeignKey(HealthFacilityAccount, on_delete=models.CASCADE)
    additionalAttributes = models.CharField(max_length=500)

class HealthCareService(models.Model):
    healthCareFacilityID = models.ForeignKey(HealthCareFacility, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    Row3 = models.CharField(max_length=100)

class ClaimRequest(models.Model):
    healthFacilityID = models.ForeignKey(HealthCareFacility, on_delete=models.CASCADE)
    requesterPhoneNumber = PhoneNumberField(null=False, blank=False)
    requesterFirstName = models.CharField(max_length=100)
    requesterLastName = models.CharField(max_length=100)
    requesterEmail = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    attachment = models.FileField()
    status = models.CharField(max_length=50)
    isDone = models.CharField(max_length=50)
    dateTime = models.DateTimeField(default=timezone.now)
    cancelDateTime = models.DateTimeField()

class Automations(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    triggers = models.CharField(max_length=100)
    actions = models.CharField(max_length=100)
    isActive = models.CharField(max_length=100)
    creationDateTime = models.DateTimeField(default=datetime.now, blank=True)
    tags = models.CharField(max_length=100)

class HeartRateHistory(models.Model):
    dateTime = models.DateTimeField()
    reading = models.CharField(max_length=100)

class SleepHistory(models.Model):
    date = models.DateTimeField()
    hours = models.TimeField()