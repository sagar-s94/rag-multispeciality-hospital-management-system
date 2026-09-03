
from django.urls import path
from . import views
urlpatterns=[
    path("doctor_dashboard/",views.docotr_dashboard,name="dr_dashboard"),
    path("logout/", views.doctor_logout, name="doctor_logout"),
    path("doctor-profile/",views.profile,name="doctor_profile"),
    path("paitent_list/",views.ipd_patient_list,name="ipd_patient_list"),
    path("make_request/",views.make_request,name="make_request"),
    path("request_list/",views.request_list,name="request_list"),
    path("edit_profile/",views.edit_profile,name="edit_profile"),
    path("edit_list/<int:id>/",views.request_edit,name="edit_rqst_list"),
    path("list_delete/<int:id>/",views.delete_request,name="list_delete"),
    path("visitors/<str:department>/",views.department_visitors,name="department_visitors"),
    
   
] 