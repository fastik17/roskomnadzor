from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, \
    BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        user = self.model(email=email, password=password)
        user.set_password(password)
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email_):
        return self.get(email=email_)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=25, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    timestamp_created = models.DateTimeField(null=True, blank=True,
                                             auto_now_add=True, )
    last_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'

    objects = UserManager()

    def __str__(self):
        return self.email
