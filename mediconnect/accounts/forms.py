from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UserChangeForm,
)
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_email(email):
    occurences = User.objects.filter(email=str(email)).count()
    if occurences:
        raise ValidationError(
            _("%(email)s is already in use! Please use a different email."),
            params={"email": email},
        )


class SignupForm(forms.Form):
    username = forms.CharField(max_length=250, required=True)
    first_name = forms.CharField(max_length=250, required=True)
    last_name = forms.CharField(max_length=250, required=True)
    email = forms.EmailField(
        max_length=200, help_text="Required", validators=[validate_email], required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "block border border-grey-light w-full p-3 rounded mb-4"
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        
        self.fields["first_name"].widget.attrs["class"] = "block border border-grey-light w-full p-3 rounded mb-4"
        self.fields["first_name"].widget.attrs["placeholder"] = "First Name"

        self.fields["last_name"].widget.attrs["class"] = "block border border-grey-light w-full p-3 rounded mb-4"
        self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"

        self.fields["email"].widget.attrs["class"] = "block border border-grey-light w-full p-3 rounded mb-4"
        self.fields["email"].widget.attrs["placeholder"] = "email_address@host.domain"



class LoginForm(AuthenticationForm):
    username_email = forms.CharField(label="Email or Username", max_length=250)

    class Meta:
        model = User
        fields = ("username_email", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = dict(reversed(list(self.fields.items())))
        self.fields.pop("username")
        self.fields["username_email"].widget.attrs[
            "placeholder"
        ] = "Type in email or username"
        self.fields["username_email"].widget.attrs["class"] = "block border border-grey-light w-full p-3 rounded mb-4"

        self.fields["password"].widget.attrs["placeholder"] = "Type in your password"
        self.fields["password"].widget.attrs["class"] = "block border border-grey-light w-full p-3 rounded mb-4"



class EditProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        if "admin" in kwargs:
            self.admin = kwargs["admin"]
            kwargs.pop("admin")
        super().__init__(*args, **kwargs)
        if "username" in self.fields:
            self.fields.pop("username")

        self.fields["first_name"].widget.attrs["class"] = "block border border-grey-light w-full p-3 rounded mb-4"
        self.fields["first_name"].widget.attrs["required"] = "true"
        self.fields["first_name"].widget.attrs["placeholder"] = "First Name"

        self.fields["last_name"].widget.attrs["class"] = "block border border-grey-light w-full p-3 rounded mb-4"
        self.fields["last_name"].widget.attrs["required"] = "true"
        self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"

        self.fields["email"].widget.attrs["class"] = "block border border-grey-light w-full p-3 rounded mb-4"
        self.fields["email"].widget.attrs["required"] = "true"
        self.fields["email"].widget.attrs["placeholder"] = "Email Address"

        if not self.admin:
            self.fields.pop("password")

    class Meta(UserChangeForm):
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )


class PasswordChangeForms(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["old_password"].widget.attrs["placeholder"] = "Current Password"
        self.fields["old_password"].widget.attrs["class"] = "block border border-grey-light w-full p-3 rounded mb-4"
        self.fields["old_password"].label = "Current Password"

        self.fields["new_password1"].widget.attrs["placeholder"] = "New Password"
        self.fields["new_password1"].widget.attrs["class"] = "block border border-grey-light w-full p-3 rounded mb-4"

        self.fields["new_password2"].widget.attrs[
            "placeholder"
        ] = "Retype the new password"
        self.fields["new_password2"].widget.attrs["class"] = "block border border-grey-light w-full p-3 rounded mb-4"