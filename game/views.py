from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User


def admin_check(user):
    print(user.username)
    print(f'user.is_authenticated = {user.is_authenticated}')
    print(f'user.is_superuser = {user.is_superuser}')
    return user.is_authenticated and user.is_superuser


@user_passes_test(admin_check)
def admin_view(request):
    # Логика для администратора
    return render(request, template_name='game/battle_field_create.html')


def user_view(request):
    # Логика для обычного пользователя
    return render(request, template_name='game/battle_field_play.html')

