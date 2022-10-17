from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("usuarios:login"))
    return render(request, "usuarios/usuario.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("usuarios:index"))
        else:
            return render(request, "usuarios/login.html", {"msj": "Credenciales incorrectas" })
    return render(request, "usuarios/login.html")


def logout_view(request):
    logout(request)
    return render(request, "usuarios/login.html", {
                "msj": "Usuario Deslogueado"})
