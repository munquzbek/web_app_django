from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, PasswordResetView1, verify, success, verify_email

from django.contrib.auth import views as auth_views

from django.views.decorators.cache import never_cache

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', never_cache(ProfileView.as_view()), name='profile'),
    path('verify/<str:token>', verify),
    path('success/', success, name='success'),
    path('verify_email/', verify_email, name='verify'),

    # password reset urls
    path('password_reset/', PasswordResetView1.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
