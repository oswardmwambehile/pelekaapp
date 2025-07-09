from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager  # Import the manager you just created

phone_validator = RegexValidator(
    regex=r'^\+255\d{9}$',
    message='Phone number must be in the format +255XXXXXXXXX (Tanzania only)'
)

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('sender', 'Sender'),
        ('transporter', 'Transporter'),
    )

    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=13,
        validators=[phone_validator],
        unique=True,
        help_text='Enter phone number in the format +255XXXXXXXXX'
    )
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=False,
        null=False,
        help_text='Upload a profile picture'
    )
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='sender',
        help_text='Select user type'
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "phone_number"]

    objects = CustomUserManager()  # ✅ Attach the custom manager here

    def __str__(self):
        return f"{self.email} ({self.user_type})"
