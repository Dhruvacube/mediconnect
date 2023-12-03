from django.conf.urls import include
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r"^profile/$", views.view_profile, name="view_profile"),
    re_path(
        r"^changepassword/$", views.change_password, name="change_password"),
    re_path(r"^login/$", views.loginform, name="signin"),
    re_path(r"^logout/$", views.user_logout, name="signout"),
    path("signup/", views.signup, name="signup"),
    path("", include("django.contrib.auth.urls")),
]