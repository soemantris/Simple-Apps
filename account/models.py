from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, nama, password):

        if not email:
            raise ValueError('Pengguna harus memiliki alamat email')

        user = self.model(
            email=self.normalize_email(email),
            nama=nama,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nama, password):
        user = self.create_user(
            email,
            password=password,
            nama=nama,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    nama = models.CharField(max_length=75)
    tmp_lahir = models.CharField(max_length=150)
    tgl_lahir = models.DateField(blank=True, default=timezone.now)
    email = models.EmailField(blank=True, unique=True)
    no_hp = models.IntegerField(blank=True, null=True)
    img_user = models.ImageField(
        blank=True, upload_to='users/', default='profile.png')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nama',]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
