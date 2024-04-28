from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    CustomUser model will be use for email authentication
    """
    email = models.EmailField(unique=True, max_length=256)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    @property
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name

    @property
    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    @property
    def birthday(self):
        """Return the humanize birth_date for the user."""

        return self.birth_date.strftime()




