from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm


@login_required(login_url="signin")
def index(request):
    return render(request, "index.html", {"range": range(10)})


def signin(request):
    form = LoginForm
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            print(user, form.cleaned_data, User.objects.all())
            if user is not None:
                login(request, user)
                return redirect(reverse("index"))

    return render(request, "form.html", {"form": form})


def register(request):
    form = RegisterForm

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("signin"))

    return render(request, "form.html", {"form": form})


def signout(request):
    logout(request)
    return redirect(reverse("signin"))
