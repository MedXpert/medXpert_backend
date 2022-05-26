import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
# Create your models here.

from .manager import CustomUserManager

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
