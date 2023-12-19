from django.db import models
from сustom_authorization.models import Profile


class Product(models.Model):
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
    name = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(default='')
    price = models.DecimalField(decimal_places=2, max_digits=10000000, default=100)


class Gift(models.Model):
    class Meta:
        verbose_name = 'подарок'
        verbose_name_plural = 'подарки'
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    is_used = models.BooleanField(default=False)


class BattleField(models.Model):
    class Meta:
        verbose_name = 'игровое поле'
        verbose_name_plural = 'игровые поля'
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    shot_coordinates = models.CharField(max_length=1024, default='')
    size_horizontal = models.IntegerField(default=10)
    size_vertical = models.IntegerField(default=10)


class Ship(models.Model):
    class Meta:
        verbose_name = 'корабль'
        verbose_name_plural = 'корабли'
    battle_field = models.ForeignKey(BattleField, on_delete=models.CASCADE)
    gift = models.ForeignKey
    coordinates = models.CharField(max_length=256, default='')
