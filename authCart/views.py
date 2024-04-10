from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate,login,logout
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import TokenGenerator, generate_token

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

        user = User.objects.create_user(email, email, password)
        user.is_active = True
        user.save()
        messages.success(request, "Account created successfully.")


        # email_subject = "Activate Your Account"
        # message = render_to_string('aunthication/activate.html', {
        #     'user': user,
        #     'domain': '127.0.0.1:8000',
        #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        #     'token': generate_token.make_token(user)
        # })

        # sending email message to user
        # email_message = EmailMessage(
        #     email_subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [email],
        # )
        # email_message.send()

        # email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
        # print("line 53")
        # email_message.send()
        # print("line 55")
        # messages.success(request, "Account created successfully. Please check your email to activate your account.")
        # return redirect("/auth/login/")


    return render(request, "aunthication/signup.html")


# class ActivateAccountView(View):
#     def get(self, request, uidb64, token):
#         try:
#             uid = force_str(urlsafe_base64_decode(uidb64))
#             user = User.objects.get(pk=uid)
#         except Exception as identifier:
#             user = None

#         if user is not None and generate_token.check_token(user, token):
#             user.is_active = True
#             user.save()
#             messages.info(request, "Account Activated Successfully")
#             return redirect('/auth/login')
#         return render(request, 'aunthication/activatefail.html')


def handle_login(request):
    if request.method=="POST":

        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')

        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/auth/login')

    return render(request, "aunthication/login.html")


def handle_logout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/auth/login')
