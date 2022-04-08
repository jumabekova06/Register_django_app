from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUserManager(BaseUserManager):

    def create_user(self, email, username, phone,password):
        email = self.normalize_email(email)
        user = self.model(email=email,phone=phone, username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', null=False, blank=False, unique=True)
    username = models.CharField(verbose_name='имя', max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=50,blank=False)
    is_staff = models.BooleanField('staff status', default=False,)
    is_active = models.BooleanField('активен', default=True)
    date_joined = models.DateTimeField('дата регистрации', default=timezone.now)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    def has_perm(self,  perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.email
