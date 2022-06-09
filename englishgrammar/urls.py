from django.urls import path
from django.contrib.auth import views as auth_views

from .views import home

from . import views

urlpatterns = [
    path('', home),
    
    path('parser/', views.parser, name='parser'),
    path('parser/parse', views.parse),
    
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='englishgrammar/password_reset.html'), name='reset_password'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name='englishgrammar/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='englishgrammar/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password/complete', auth_views.PasswordResetCompleteView.as_view(template_name='englishgrammar/password_reset_complete.html'), name='password_reset_complete'),
    
    path('dashboard', views.dashboard, name='dashboard'),
]