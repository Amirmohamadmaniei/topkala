from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError('شماره تلفن الزامی است')

        user = self.model(phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        if not phone:
            raise ValueError('شماره تلفن الزامی است')

        user = self.create_user(phone, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
