import random
import string

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):

    def create_user(self, email, phone_number, password=None, username=None, user_surname=None, nickname=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not phone_number:
            raise ValueError('Users must have a phone number')

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            username=username,
            user_surname=user_surname,
            nickname=nickname
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password):
        user = self.create_user(
            email=self.normalize_email(email),
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField(max_length=255, null=True, blank=True, unique=True)
    username = models.CharField(max_length=255, null=True, blank=True, unique=False)
    user_surname = models.CharField(max_length=255, null=True, blank=True, unique=False)
    phone_number = models.CharField(max_length=255, null=False, blank=False, unique=True)
    email = models.EmailField('email address', unique=True)
    password = models.CharField(max_length=255, null=False, blank=False)
    check_code = models.CharField(max_length=17, null=True, blank=True, unique=True)

    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'

    def create_activation_code(self):
        from django.utils.crypto import get_random_string
        code = get_random_string(20)
        self.otp = code
        self.save()
        return code

    def generate_mixed_text(self):

        part1 = random.choice(string.ascii_uppercase) + ''.join(random.choice(string.digits) for _ in range(2))

        part2 = random.choice(string.ascii_uppercase) + ''.join(random.choice(string.digits) for _ in range(3))

        part3 = random.choice(string.ascii_uppercase) + ''.join(random.choice(string.digits) for _ in range(3))

        part4 = random.choice(string.ascii_uppercase) + ''.join(random.choice(string.digits) for _ in range(2))

        mixed_text = f"{part1}-{part2}-{part3}-{part4}"

        self.check_code = mixed_text
        self.save()
        return mixed_text
