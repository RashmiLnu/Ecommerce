from django.urls import path
from authCart import views

urlpatterns = [
   path("signup/", views.signUp , name="signUp"),
   path("login/", views.login , name="login"),
   path("logout/", views.logout , name="logout"),
]