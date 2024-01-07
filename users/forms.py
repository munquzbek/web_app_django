from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'country', 'avatar',)

    def __init__(self, *args, **kwargs):
        """This need to do not show:
        "No password set.
        Raw passwords are not stored, so there is no way to see this user’s password,
        but you can change the password using this form."
        This message when updating profile
        """
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
