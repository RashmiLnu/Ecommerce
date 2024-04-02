from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def signUp(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["pass1"]
        confirm_password = request.POST["pass2"]
        if password != confirm_password:
            messages.warning(request, "Passwords do not match")
            return render(request, "aunthication/signUp.html")

        try:
            User.objects.get(username=email)
            messages.warning(request, "User already exists")
            return render(request, "aunthication/signUp.html")

        except Exception as identifier:
            pass

        user = User.objects.create_user(email,email,password)
        user.save()
        messages.success(request, "User created successfully")
    
    return render(request, "aunthication/signUp.html")


def login(request):
    return render(request, "aunthication/login.html")

def logout(request):
    return redirect("login")
