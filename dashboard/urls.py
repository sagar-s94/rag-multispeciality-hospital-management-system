from django.urls import path
from . import views

urlpatterns = [
    path("",views.dashboard,name="dashboard"),
    path("appointments/",views.appointments,name="appoint"),
    path("ambulance_list/",views.list_ambulance,name="list")
]