from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from game.views import admin_check


# Create your views here.
def authorization_view(request):
    is_auth = request.user.is_authenticated
    if is_auth:
        print('redirect to authorization_completed')
        redirect('authorization_completed')
    return render(request=request,
                  template_name='authorization/authorization.html')


def authorization_completed(request):
    print('authorization_completed')
    if admin_check(request.user):
        print('redirect(\'admin_view\')')
        return redirect('admin_view')
    else:
        print('redirect(\'user_view\')')
        return redirect('user_view')


def registration(request):
    return render(template_name='authorization/registration.html')
