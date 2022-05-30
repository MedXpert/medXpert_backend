from lib2to3.pytree import Base
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The email must be set"))
        if not password:
            raise ValueError(_("The password must be set"))
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('isActive', True)
        extra_fields.setdefault('role', 'ad')

        if extra_fields.get('role') != 'ad':
            raise ValueError('Superuser must have role of Global Admin')
        return self.create_user(email, password, **extra_fields)