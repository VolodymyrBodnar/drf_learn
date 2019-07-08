from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):
    """
    Manager for custom user model
    """
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('role', 1)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('role', 2)

        if extra_fields.get('role') != 2:
            raise ValueError('Superuser must have role = 2.')
        else:
            extra_fields.setdefault('is_superuser', True)
            extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    User model
    """

    ROLE_CHOICES = [
        (1, 'common user'),
        (2, 'admin')
    ]

    username = None

    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(('first name'), max_length=45, blank=True)
    last_name = models.CharField(('last name'), max_length=45, blank=True)

    birth_date = models.DateField(
        ('birth_date'), auto_now=False, auto_now_add=False, blank=True, null=True)

    is_active = models.BooleanField(('active'), default=True)
    role = models.IntegerField(verbose_name=('Current Role'), choices=ROLE_CHOICES, default=1,
                               help_text=("Store current user role in system, "))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __repr__(self):
        """
        representation for user model
        """
        return f'{self.first_name} {self.last_name}.'
