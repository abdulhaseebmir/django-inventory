from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(f"Username: {username} - Password: {password}")
        user = authenticate(request, username=username, password=password)
        if not user:
            context = {
                "error": "Invalid username or password"
            }
            return render(request, "accounts/login.html", context)
        login(request, user)
        return redirect("/")
    return render(request, "accounts/login.html", {})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html", {})