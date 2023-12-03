from asgiref.sync import sync_to_async
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Q
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .templatetags import *
from .forms import (
    EditProfileForm,
    LoginForm,
    PasswordChangeForms,
    SignupForm,
)
from .tokens import account_activation_token


@sync_to_async
@login_required
def view_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST,instance=request.user,admin=False)

        if form.is_valid():
            form.save(commit=True)
            messages.success(request,"Your Profile has been update successfully !")
            return redirect(reverse("view_profile"))
        if not form.errors:
            messages.error(request, "Please correct the errors mentioned below!")

    else:
        form = EditProfileForm(instance=request.user, admin=False)
    return render(
        request,
        "profile.html",
        {
            "form": form,
        },
    )


@sync_to_async
@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForms(data=request.POST, user=request.user)

        if form.is_valid():
            messages.success(
                request,
                "Your password has been update successfully !"
            )
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponsePermanentRedirect(reverse("change_password"))
        messages.error(request, "Please correct the errors mentioned below!")
    else:
        form = PasswordChangeForms(user=request.user)
    return render(
        request,
        "registration/password_reset_confirm.html",
        {
            "form": form,
        },
    )


@sync_to_async
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out!")
    return HttpResponsePermanentRedirect(reverse("home"))


@sync_to_async
def loginform(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)

        username_email = request.POST.get("username_email")
        user_obj = User.objects.filter(Q(username=username_email) | Q(email=username_email))
        if not user_obj.exists():
            messages.warning(request, "Please create an new account !")
            return redirect(reverse("signup"))
        if form.is_valid():
            username = user_obj.all()[0].username
            password = form.cleaned_data.get("password")
            next_url = request.POST.get("next")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                messages.success(request, "You have been successfully logged in!")
                login(request, user)
                if bool(next_url):
                    return HttpResponsePermanentRedirect(next_url)
                return HttpResponsePermanentRedirect(reverse("home"))
            messages.error(request, "Invalid username or password.")
            return redirect(reverse("signin"))
        messages.error(request, "Details Invalid")
        return redirect(reverse("signin"))
    form = LoginForm()
    return render(
        request,
        "login.html",
        {
            "form": form,
            "next": request.GET.get("next")
        },
    )


@sync_to_async
def signup(request):
    current_site = get_current_site(request)
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(**data)
            user.save()
            to_email = form.cleaned_data.get("email")
            ctx = {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": account_activation_token.make_token(user),
                "username": form.cleaned_data.get("username"),
                "protocol": "https" if request.is_secure() else "http",
            }
            return redirect(reverse("home"))
    form = SignupForm()
    return render(
        request,
        "signup.html",
        {
            "form": form,
            "link": f'{reverse("signin")}',
        },
    )