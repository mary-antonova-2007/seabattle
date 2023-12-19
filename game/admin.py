from django.contrib import admin

# Register your models here.
from game.models import BattleField, Ship, Gift, Product

admin.site.register(BattleField)
admin.site.register(Ship)
admin.site.register(Gift)
admin.site.register(Product)

