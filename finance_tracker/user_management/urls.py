from django.urls import path
from django.contrib.auth import views as auth_views  
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register_user, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Используем стандартное представление для входа
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Используем стандартное представление для выхода
]
