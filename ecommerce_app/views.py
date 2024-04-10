from django.shortcuts import render
from ecommerce_app.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("pnumbers")
        message = request.POST.get("message")
        myquesry = Contact(name=name, email=email, phone=phone, message=message)
        myquesry.save()
        messages.info(request, "Thank you for contacting us. We will get back to you soon.")
        return render(request, "contact.html")

    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")
