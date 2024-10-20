from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('business', 'Business'),
    ]
    
    username = None
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='individual')
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    address = models.TextField(blank=False, null=False)

    # Business-specific fields
    business_name = models.CharField(max_length=255, blank=True, null=True)
    vat_number = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = "custom_user"
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.email
