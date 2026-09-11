from django.urls import path
from . import views

urlpatterns = [
    path("receptionist_dashboard/",views.recep_home,name="recep_home"),
    path("Appointment-list/", views.appoint_list, name="appoint_list"),
    path("add_opd/",views.add_opd,name="add_opd"),
    path("opd_list/",views.opd_list,name="opd_list"),
    path("update_opd/",views.Update_opd,name="updateopd"),
    path("edit_opd/<int:id>/",views.edit_opd,name="edit_opd"),
    path("opd/delete/<str:patient_id>/", views.delete_opd, name="delete_opd"),

    path("generate_invoice/<str:patient_id>/",views.generate_invoice,name="generate_invoice"),

    #ambulaance
    path("add_ambulance/",views.add_ambulance,name="add_ambulance"),
    path("ambulance-list/", views.ambulance_list, name="ambulance_list"),
    path("ambulance_delete/<int:id>/",views.delete_ambulance,name="ambulance_delete"),
    
    #Vistors
    path("add-visitor/", views.add_visitor, name="add_visitor"),
    path("visitor-list/", views.visitor_list, name="visitor_list"),
    path("edit-visitor/<int:visitor_id>/",views.edit_visitor,name="edit_visitor"),
    path("delete-visitor/<int:visitor_id>/",views.delete_visitor,name="delete_visitor"),

    #service_slip
    path("service-slip/<int:id>/",views.service_slip,name="service_slip"),
]
