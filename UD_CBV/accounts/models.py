from django.db import models
#ユーザをカスタマイズ用のモデルを作成する
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin

)
from django.urls import reverse_lazy
# Create your models here.

#create用
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Enter Email")
        user = self.model(
            username=username,
            email = email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

#カスタマイズ用
class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    is_active=models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
#ユーザを一意に識別
    USERNAME_FIELD = "email"
#スーパーユーザ作成に必要なフィールド
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def get_absolute_url(get):
        return reverse_lazy("accounts:home")



