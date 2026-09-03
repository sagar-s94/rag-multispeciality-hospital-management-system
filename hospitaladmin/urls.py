from django.urls import path,include
from . import views
urlpatterns = [
    
   path("Admin_Home/",views.home_page,name="Admin_home"),
   path("Admin_register/",views.register_admin,name="admin_register"),
   path("add_doctors/",views.add_doctors,name="add_doctors"),
   path("doctor_list/",views.doctor_list,name="doctor_list"),
   path("doctor_update/",views.update_dr,name="update_dr"),
   path("view_dr/<int:doctor_id>/",views.view_doctor,name="view_dr"),
   path("doctor-update/<int:doctor_id>/",views.edit_dr,name="doctor_update"),
   path("doctor_delete/<int:doctor_id>/",views.delete_dr,name="delete_dr"),

   #nurse
   path("Add_nurse/",views.Add_nurse,name="add_nurse"),
   path("nurse_list/",views.nurse_list,name="nurse_list"),
   path("nurse-view/<int:id>/",views.view_nurse,name="nurse-view"),
   path("update_nurse/",views.update_nurse,name="update_nurse"),
   path("nurse-edit/<int:id>/",views.edit_nurse,name="edit_nurse"),
   path("delete_nurse/<int:id>/",views.delete_nurse,name="delete_nurse"),

   #departments

   path("dept_dashboard/",views.dpt_dashboard,name="dept_dashboard"),
   path("general_ward/",views.general_ward_dashboard,name="general_ward"),
   path("general_ipd_patients/",views.genral_ipd,name="ipd_general"),
   path("general_ipd_list/",views.general_ipd_list,name="general_ipd_list"),
   path("genral_ipd_view/<int:id>/",views.general_ipd_view,name="general_ipd_view"),
   path("general-ward/ipd/edit/<int:id>/",views.edit_view,name="edit_general_ipd"),
   path("general-ward-ipd_delte/<int:id>/",views.delete_ipd_patients,name="general_ipd_delete"),

   #rooms
   path("add-room/", views.add_rooms, name="add_rooms"),
   path("room_list/",views.room_list,name="room_list"),
   path("edit-room/<int:id>/", views.edit_room, name="edit_room"),
   path("delete_room/<int:id>/",views.delete_room,name="delete_room"),

   #ward_suport_staff
   path("support_staff/",views.Ward_Support_Staff,name="genral_support_staff"),
   path("suport_staff_list/",views.Ward_Staff_list,name="suport_staff_list"),
   path("edit_staff/<int:id>/",views.edit_staff,name="edit_staff"),
   path("delete_staff/<int:id>/",views.delete_staff,name="delete_staff"),

   #wards
   path("cardic_ward/",views.cardic_ward_dashboard,name="cardic_ward"),
   path("neuro_ward/",views.neuro_ward_dashboard,name="neuro_ward"),
   path("orthopedic_ward/",views.orthopedic_dasboard,name="orthopedic_ward"),
   path("child_ward/",views.childcare_dashbaord,name="child_care_ward"),
   path("women_ward/",views.women_dashboard,name="women_ward"),
   path("gastro_ward/",views.gastro_ward,name="gastro_ward"),
   path("ent_eye_ward/",views.ent_eye_ward,name="ent_eye_ward"),
   path("skin_allergy_ward/",views.skin_allery_ward,name="skin_allery_ward"),
   path("surgery_ward/",views.surgery_ward,name="surgery_ward"),

   #annoucements
   path("announcement/create/",views.create_announcement,name="create_announcement"),
   path("announcment_list/",views.annoucemnt_list,name="announcemt_list"),
   path("announcement/edit/<int:id>/",views.edit_announcement,name="edit_announcement"),
   path("announcement/delete/<int:id>/",views.delete_announcement,name="delete_announcement"),

   #lab_technician
   path("lab_home/",views.lab_home,name="lab_home"),
   path("lab/upload-report/<int:request_id>/",views.upload_lab_report,name="upload_report"),
 

]