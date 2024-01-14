from catalog.views import UserIsVerified
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail

from django.contrib.auth.mixins import LoginRequiredMixin


def verify_email(request):
    context = {
        'title': 'Verify email'
    }
    return render(request, 'users/verify_email.html', context)


def success(request):
    context = {
        'title': 'Success sign up'
    }
    return render(request, 'users/success.html', context)


def verify(request, token):
    try:
        user = get_object_or_404(User, token=token)
        if user:
            user.is_verified = True
            user.save()
            print(user.__dict__)
            msg = 'Your email verified'
            return render(request, 'info.html', {'msg': msg})
    except Exception as e:
        msg = e
        return render(request, 'info.html', {'msg': msg})


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:success')

    def form_valid(self, form):
        self.object = form.save()
        domain_name = get_current_site(self.request).domain
        print(self.object)
        print(f'token user {self.object.token}')
        link = f'http://{domain_name}/users/verify/{str(self.object.token)}'
        print(link)

        send_mail(
            "Email Verification",
            f"Click the link-> {link} to verify",
            settings.EMAIL_HOST_USER,
            [self.object.email],
            fail_silently=False,
        )
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, UserIsVerified, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        """this need to do not provide pk to update profile"""
        return self.request.user


class PasswordResetView1(LoginRequiredMixin, UserIsVerified, PasswordResetView):
    from_email = settings.EMAIL_HOST_USER
    success_url = reverse_lazy("users:password_reset_done")


