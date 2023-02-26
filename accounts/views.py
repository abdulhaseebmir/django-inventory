from django.shortcuts import render

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(f"Username: {username} - Password: {password}")
    return render(request, "accounts/login.html", {})