
import uuid

from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from pkg_resources import require


# Create your models here.

from .manager import CustomUserManager


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

class User(AbstractBaseUser, PermissionsMixin):

    ADMIN = 'ad'
    HEALTHFACILITY = 'h'
    AMBULANCE = 'am'
    USER = 'u'

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (HEALTHFACILITY, 'HealthFacility'),
        (AMBULANCE, 'Ambulance'),
        (USER, 'User'),
    )

    MALE = 'm'
    FEMALE = 'f'

    SEX_CHOICES = (
        (MALE, "male"),
        (FEMALE, "female")
    )

     # Roles created here
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    email = models.EmailField(unique=True)
    username = None
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=10, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=MALE, null=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    # profilePicture = models.ImageField(upload_to='profile_pics', blank=True)
    role = models.CharField(choices=ROLE_CHOICES, null=True, default=USER, max_length=3)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    createdDate = models.DateTimeField(default=timezone.now)
    modifiedDate = models.DateTimeField(default=timezone.now)
    createdBy = models.EmailField()
    modifiedBy = models.EmailField()

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class HealthFacilityAccount(models.Model):
    healthFacilityOrAmbulanceID = models.ForeignKey('api.AmbulanceService', on_delete=models.CASCADE)
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
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    CANCELLED_BY_CHOICES = (
        ('user', 'User'),
        ('healthfacility', 'HealthFacility'),
    )

    userID = models.ForeignKey(User, on_delete=models.CASCADE) # This line should be uncommented when the Users class is added
    healthFacilityID = models.ForeignKey(HealthCareFacility, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(require=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    reminderStatus = models.BooleanField(default=False)
    cancelledBy = models.CharField(max_length=50, choices=CANCELLED_BY_CHOICES, default='user', null=True)

class UserRating(models.Model):
    #userID = models.ForeignKey(Users, on_delete=models.CASCADE) # This line should be uncommented when the Users class is added
    healthFacilityID = models.ForeignKey(HealthCareFacility, on_delete=models.CASCADE)
    rating = models.IntegerField()
    healthFacilityType = models.CharField(max_length=100)
    creationDateTime = models.DateTimeField(default=datetime.now, blank=True)
    lastUpdateTime = models.DateTimeField(default=datetime.now, blank=True)

class UserReview(models.Model):
    #userID = models.ForeignKey(Users, on_delete=models.CASCADE) # This line should be uncommented when the Users class is added
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


