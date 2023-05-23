from django.db import models
from django.urls import reverse
from common.models import TimeStampedModel
from users.managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser




class CustomUser(TimeStampedModel, AbstractBaseUser, PermissionsMixin):
    username = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ('-last_name',)
    
    def get_full_name(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    def __str__(self):
        return f"{self.get_full_name()}"

    def get_absolute_url(self):
       return reverse("user_detail", kwargs={"id": self.id})
    
   
