from random import randint

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from apps.users.manager import UserManager


class CustomUserProfile(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    email_comfirmed = models.BooleanField(default=False)
    email_verification_code = models.CharField(max_length=6, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return self.email


class ActivationCode(models.Model):
    user = models.OneToOneField(CustomUserProfile, on_delete=models.CASCADE)
    activation_code = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.code = randint(100000, 999999)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email} - {self.code}"

    def create_activation_code(self):
        self.activation_code = randint(100000, 999999)
        self.save()
        return self.activation_code

    def verify_activation_code(self, code):
        if code == self.activation_code:
            self.user.email_comfirmed = True
            self.user.save()
            return True
        return False
