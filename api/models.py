import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
# Create your models here.

from .manager import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):

    ADMIN = 1
    HEALTHFACILITY = 2
    AMBULANCE = 3
    USER = 4

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
    username = models.CharField(unique=True, max_length=255)
    firstName = models.CharField(max_length=30, blank=True)
    lastName = models.CharField(max_length=50, blank=True)
    phoneNumber = models.CharField(max_length=10, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=MALE, null=True)
    dateOfBirth = models.DateField(blank=True)
    # profilePicture = models.ImageField(upload_to='profile_pics', blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    createdDate = models.DateTimeField(default=timezone.now)
    modifiedDate = models.DateTimeField(default=timezone.now)
    createdBy = models.EmailField()
    modifiedBy = models.EmailField()

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
