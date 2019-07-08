from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User model
    """

    ROLE_CHOICES = [
        (1, 'common user'),
        (2, 'admin')
    ]

    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    is_active = models.BooleanField(('active'), default=True)

    def __repr__(self):
        """
        representation for user model
        """
        return f'{self.first_name} {self.last_name}.'
