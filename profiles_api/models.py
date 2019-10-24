from django.db import models
from django.contrib.models import AbstractBaseUser, PermissionsMixin


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database user model in the system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_lenght=255)
    is_active = models.BooleanFiel(default=True)
    is_staff = models.BooleanFiel(default=False)

    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrieves full username """
        return self.name

    def get_short_name(self):
        """ Retrieves short username """
        return self.name

    def __str__(self):
        """ Retuen string representation from an user """
        return self.email;


