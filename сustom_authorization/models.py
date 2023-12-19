from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'
    user = models.OneToOneField(User, verbose_name='имя пользователя', on_delete=models.CASCADE)
    shot_attempts = models.IntegerField(verbose_name='количество попыток')
    user_image = models.ImageField(verbose_name='аватар')
