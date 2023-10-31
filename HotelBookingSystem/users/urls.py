from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
   path('user-profile/', views.profile, name='profile'),
   path('login/', views.CustomLoginView.as_view(), name='login'),
   path('logout/', views.logout_user, name='logout-user'),
   path('register/', views.SignUpView.as_view(), name='register'),
   path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'), name='password-reset'),
   path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), name='password_reset_done'),
   path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
   path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), name='password_reset_complete'),   

]