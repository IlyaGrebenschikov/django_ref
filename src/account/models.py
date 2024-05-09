from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models


class MyUser(User):
    referred_by = models.CharField(default=None, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'Имя: {self.username}, email: {self.email}'

    def get_absolute_url(self):
        return reverse("user-details", kwargs={"pk": self.pk})
