from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, MessageForm, RegisterForm
from .models import Chat, Message


@login_required(login_url="signin")
def index(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, "index.html", {"users": users})


@login_required(login_url="signin")
def chat(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    chat = Chat.objects.filter(users=user).filter(users=request.user).first()
    if chat is None:
        chat = Chat.objects.create()
        chat.users.add(user)
        chat.users.add(request.user)

    form = MessageForm
    if request.method == "POST":
        message = Message(chat=chat, user=user)
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect(reverse("chat", kwargs={"user_id": user.id}))

    return render(
        request,
        "chat.html",
        {"messages": chat.message_set.all(), "form": form},
    )


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
