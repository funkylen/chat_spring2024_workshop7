from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("signin", views.signin, name="signin"),
    path("register", views.register, name="register"),
    path("logout", views.signout, name="signout"),
]
