from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import COUNTRIES, COUNTRY_CODES


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Поле 'email' обязательно для заполнения.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Класс для создания пользователя."""

    username = models.CharField(
        max_length=50, verbose_name="имя пользователя", help_text="Введите имя пользователя", null=True, blank=True
    )
    email = models.EmailField(unique=True, verbose_name="email", help_text="Введите свой email")
    avatar = models.ImageField(
        upload_to="users/",
        verbose_name="фото",
        help_text="Загрузите фото",
        null=True,
        blank=True,
    )
    phone_code = models.CharField(
        max_length=5,
        choices=COUNTRY_CODES,
        verbose_name="код страны",
        help_text="Выберите код страны",
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        max_length=20,
        choices=COUNTRY_CODES,
        verbose_name="номер телефона",
        help_text="Введите номер телефона",
        null=True,
        blank=True,
    )
    country = models.CharField(
        max_length=30, choices=COUNTRIES, verbose_name="страна", help_text="Выберите страну", null=True, blank=True
    )
    token = models.CharField(max_length=100, verbose_name="токен", null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username if self.username else self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
