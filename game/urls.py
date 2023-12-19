from django.urls import path
from . import views  # Импорт представлений из вашего приложения

urlpatterns = [
    path('admin-view/', views.admin_view, name='admin_view'),
    path('user-view/', views.user_view, name='user_view'),

]
