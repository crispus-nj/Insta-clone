from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class Account(BaseUserManager):
    def create_user(self, email, username, fullname, password=None):
        user = self.model(
            email = email,
            username = username,
            fullname = fullname
        )
        user.set_password(password) 
        user.save(using = self._db)

        return user
    def create_superuser(self, email, username, fullname, password):
        user = self.create_user(
            email = email,
            username = username,
            fullname = fullname,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True

        user.save(using = self._db)
        return user

class UserAccount(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=50, unique=True)
    fullname = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'fullname']
    objects = Account()

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def has_module_perms(self, add_label):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True