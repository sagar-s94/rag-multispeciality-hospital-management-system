from django.urls import path
from . import views

urlpatterns = [
  path("registerform/",views.register,name="register_form"),
  path("login/",views.login_form,name="login_form"),
  path("logout/", views.user_logout, name="logout")
]