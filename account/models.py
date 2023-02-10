from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    phone = models.CharField(max_length=11, unique=True, verbose_name='موبایل')
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name='ایمیل')

    card_number = models.CharField(max_length=16, null=True, blank=True, verbose_name='شماره کارت بانکی')

    f_name = models.CharField(max_length=65, null=True, blank=True, verbose_name='نام')
    l_name = models.CharField(max_length=65, null=True, blank=True, verbose_name='نام خانوادگی')
    birth_day = models.DateField(null=True, blank=True, verbose_name='تاریخ تولد')

    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_admin = models.BooleanField(default=False, verbose_name='ادمین')

    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def get_full_name(self):
        if self.f_name and self.l_name:
            return f'{self.f_name} {self.l_name}'
        if self.f_name:
            return self.f_name
        if self.l_name:
            return self.l_name
        return 'نامشخص'


class OTP(models.Model):
    code = models.CharField(max_length=4, verbose_name='کد')
    phone = models.CharField(max_length=11, verbose_name='موبایل')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'OTP'
        verbose_name_plural = 'OTPs'

    def __str__(self):
        return f'{self.code} - {self.phone}'
