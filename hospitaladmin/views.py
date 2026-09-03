from django.shortcuts import render,redirect,get_object_or_404
from accounts.forms import userRegisterForm
from django.db.models import Q
from .forms import DoctorForm
from .forms import NurseForm

from .models import Doctor
from .models import Nurse
from .models import General_IPDPatient
from .models import WardBed
from .models import WardSupportStaff
from accounts.models import register_data
from doctor.models import ServiceRequest


from django.contrib import messages
from .models import Announcement
from django.contrib.auth.decorators import login_required


# Create your views here
def home_page(request):
    return render(request,"admin_home.html")

def register_admin(request):
    form = userRegisterForm(request.POST or None, request.FILES or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            
    return render(request,"registr_form.html",{"form": form})

def add_doctors(request):
    form = DoctorForm(request.POST or None, request.FILES or None)

    if request.method == "POST":

        if form.is_valid():

            form.save()

            return redirect("doctor_list")

    return render(request,"doctors/add_dr.html", {"form": form})

def doctor_list(request):
    dr_list= Doctor.objects.all()
    context={"dr_list":dr_list}
    return render(request,"doctors/doctor_list.html",context)


def update_dr(request):
    

    first_name = request.GET.get("first_name")
    department = request.GET.get("department")

    dr_list = Doctor.objects.all()

    if first_name or department:

        dr_list = Doctor.objects.filter(
            first_name__icontains=first_name or "",
            department__icontains=department or ""
        )

        if dr_list.exists():
            messages.success(request,"Doctor found successfully.")
        else:
            messages.error(request,"Doctor not found.")

    context = {
        "dr_list": dr_list
    }

    return render(request, "doctors/update_dr.html",context)


def view_doctor(request,doctor_id):

    doctor=Doctor.objects.get(doctor_id=doctor_id)

   
    return render (request,"doctors/view_dr.html",{"doctor":doctor})

def edit_dr(request,doctor_id):
    edit=Doctor.objects.get(doctor_id=doctor_id)
    if request.method == "POST":
        

        edit.first_name=request.POST.get("first_name")
        edit.last_name=request.POST.get("last_name")
        edit.gender=request.POST.get("gender")
        edit.date_of_birth=request.POST.get("date_of_birth")
        edit.profile_image=request.FILES.get("profile_image")
        edit.specialization=request.POST.get("specialization")
        edit.department=request.POST.get("department")
        edit.qualification=request.POST.get("qualification")
        edit.experience=request.POST.get("experience")
        edit.registration_no=request.POST.get("registration_no")
        edit.joining_date=request.POST.get("joining_date")
        edit.phone=request.POST.get("phone")
        edit.email=request.POST.get("email")
        edit.address=request.POST.get("address")
        edit.city=request.POST.get("city")
        edit.state=request.POST.get("state")
        edit.pincode=request.POST.get("pincode")
        edit.room_no=request.POST.get("room_no")
        edit.consultation_fee=request.POST.get("consultation_fee")
        edit.available_days=request.POST.get("available_days")
        edit.status=request.POST.get("status")
        edit.start_time=request.POST.get("start_time")
        edit.end_time=request.POST.get("end_time")

        edit.save()

        return redirect("update_dr")


    return render(request,"doctors/edit_dr.html", {"doctor":edit})


def delete_dr(request,doctor_id):
    dr=Doctor.objects.get(doctor_id=doctor_id)
    dr.delete()
    return redirect("doctor_list")

def dpt_dashboard(request):
    return render(request,"departments/dpt_dashboard.html")

def general_ward_dashboard(request):
    return render(request,"departments/gen_ward.html")

def Add_nurse(request):
    form = NurseForm(
        request.POST or None,
        request.FILES or None
    )

    if request.method == "POST":

        if form.is_valid():
            form.save()

            return redirect("nurse_list")
    return render(request,"nurses/add_nurse.html")

def nurse_list(request):
    nurses=Nurse.objects.all()
    context={ "nurses": nurses}
    return render (request,"nurses/nurse_list.html",context)

def view_nurse(request,id):
    view=Nurse.objects.get(id=id)

    context={"view":view}
    return render(request,"nurses/view_nurse.html",context)

def update_nurse(request):
    update=Nurse.objects.all()
    search=request.GET.get("search")
    if search:
        update=Nurse.objects.filter(Q(first_name__icontains=search) |
                                    Q(last_name__icontains=search) |
                                    Q(registration_no__icontains=search) |
                                    Q(qualification__icontains=search) |
                                    Q(designation__icontains=search) |
                                    Q(department__icontains=search) |
                                    Q(ward__icontains=search) |
                                    Q(phone__icontains=search) |
                                    Q(email__icontains=search))

    context={"update":update}

    return render(request,"nurses/update_nurse.html",context)

def edit_nurse(request,id):
    edit = get_object_or_404(Nurse, id=id)
    if request.method == "POST":

        edit.first_name = request.POST.get("first_name")
        edit.last_name = request.POST.get("last_name")
        edit.gender = request.POST.get("gender")
        edit.date_of_birth = request.POST.get("date_of_birth")

        edit.registration_no = request.POST.get("registration_no")
        edit.qualification = request.POST.get("qualification")
        edit.specialization = request.POST.get("specialization")
        edit.experience = request.POST.get("experience")
        edit.designation = request.POST.get("designation")
        edit.joining_date = request.POST.get("joining_date")

        edit.department = request.POST.get("department")
        edit.ward = request.POST.get("ward")
        edit.room_no = request.POST.get("room_no")
        edit.shift = request.POST.get("shift")
        edit.start_time = request.POST.get("start_time")
        edit.end_time = request.POST.get("end_time")
        edit.employment_type = request.POST.get("employment_type")
        edit.status = request.POST.get("status")

        edit.phone = request.POST.get("phone")
        edit.email = request.POST.get("email")
        edit.address = request.POST.get("address")
        edit.city = request.POST.get("city")
        edit.state = request.POST.get("state")
        edit.pincode = request.POST.get("pincode")

        if request.FILES.get("profile_image"):
            edit.profile_image = request.FILES.get("profile_image")

        edit.save()

        return redirect("update_nurse")

    context = {
        "edit": edit
        }

    return render(request,"nurses/edit_nurse.html",context)


def delete_nurse(request,id):
    nurse=Nurse.objects.get(id=id)
    nurse.delete()
    return redirect("nurse_list")

def genral_ipd(request):
    if request.method == "POST":

        General_IPDPatient.objects.create(
            ipd_number=request.POST.get("ipd_number"),

            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            gender=request.POST.get("gender"),
            date_of_birth=request.POST.get("date_of_birth") or None,
            age=request.POST.get("age"),
            blood_group=request.POST.get("blood_group"),

            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
            city=request.POST.get("city"),

            admission_date=request.POST.get("admission_date"),
            admission_time=request.POST.get("admission_time"),
            admission_type=request.POST.get("admission_type"),

            doctor=request.POST.get("doctor"),
            department=request.POST.get("department"),
            ward=request.POST.get("ward"),
         
            room_no=request.POST.get("room_no"),
            bed_no=request.POST.get("bed_no"),
            referred_by=request.POST.get("referred_by"),

            chief_complaint=request.POST.get("chief_complaint"),
            symptoms=request.POST.get("symptoms"),
            diagnosis=request.POST.get("diagnosis"),
            allergies=request.POST.get("allergies"),
            medical_history=request.POST.get("medical_history"),
            current_medication=request.POST.get("current_medication"),
            patient_condition=request.POST.get("patient_condition"),

            emergency_contact_name=request.POST.get(
                "emergency_contact_name"
            ),
            emergency_contact_relation=request.POST.get(
                "emergency_contact_relation"
            ),
            emergency_contact_phone=request.POST.get(
                "emergency_contact_phone"
            ),

            payment_type=request.POST.get("payment_type"),
            insurance_company=request.POST.get("insurance_company"),
            policy_number=request.POST.get("policy_number"),

            status=request.POST.get("status"),
            expected_discharge_date=(
                request.POST.get("expected_discharge_date") or None
            ),
            discharge_date=(
                request.POST.get("discharge_date") or None
            ),
            discharge_notes=request.POST.get("discharge_notes"),
        )

        return redirect("general_ipd_list")


    return render(request,"departments/gen_ipdpatient.html")

def general_ipd_list(request):
    patient=General_IPDPatient.objects.all()
    context={"patient":patient}
    return render(request,"departments/gen_ipdlist.html",context)

def general_ipd_view(request,id):
    patientid=General_IPDPatient.objects.get(id=id)
    context={"patientid":patientid}
    return render(request,"departments/ipdview.html",context)

def edit_view(request,id):
    edit=General_IPDPatient.objects.get(id=id)
    if request.method == "POST":

        edit.ipd_number = request.POST.get("ipd_number")
        edit.first_name = request.POST.get("first_name")
        edit.last_name = request.POST.get("last_name")
        edit.gender = request.POST.get("gender")
        edit.date_of_birth = request.POST.get("date_of_birth") or None
        edit.age = request.POST.get("age")
        edit.blood_group = request.POST.get("blood_group")

        edit.phone = request.POST.get("phone")
        edit.address = request.POST.get("address")
        edit.city = request.POST.get("city")

        edit.admission_date = request.POST.get("admission_date")
        edit.admission_time = request.POST.get("admission_time")
        edit.admission_type = request.POST.get("admission_type")

        edit.doctor = request.POST.get("doctor")

        # General Medicine Ward
        edit.ward = "General Medicine Ward"

        edit.room_no = request.POST.get("room_no")
        edit.bed_no = request.POST.get("bed_no")
        edit.referred_by = request.POST.get("referred_by")

        edit.chief_complaint = request.POST.get("chief_complaint")
        edit.symptoms = request.POST.get("symptoms")
        edit.diagnosis = request.POST.get("diagnosis")
        edit.allergies = request.POST.get("allergies")
        edit.medical_history = request.POST.get("medical_history")
        edit.current_medication = request.POST.get("current_medication")
        edit.patient_condition = request.POST.get("patient_condition")

        edit.emergency_contact_name = request.POST.get(
            "emergency_contact_name"
        )

        edit.emergency_contact_relation = request.POST.get(
            "emergency_contact_relation"
        )

        edit.emergency_contact_phone = request.POST.get(
            "emergency_contact_phone"
        )

        edit.payment_type = request.POST.get("payment_type")
        edit.insurance_company = request.POST.get(
            "insurance_company"
        )
        edit.policy_number = request.POST.get(
            "policy_number"
        )

        edit.status = request.POST.get("status")

        edit.expected_discharge_date = (
            request.POST.get("expected_discharge_date")
            or None
        )

        edit.discharge_date = (
            request.POST.get("discharge_date")
            or None
        )

        edit.discharge_notes = request.POST.get(
            "discharge_notes"
        )

        edit.save()
        return redirect(
            "general_ipd_view",
            id=edit.id
        )

    context = {
        "edit": edit
    }

  
    return render(request,"departments/edit_ipd.html",context)

def delete_ipd_patients(request,id):
    delete_idd=General_IPDPatient.objects.get(id=id)
    delete_idd.delete()
    return redirect("general_ipd_list")

def add_rooms(request):
    if request.method == "POST":

        room_number = request.POST.get("room_number")
        bed_number = request.POST.get("bed_number")
        status = request.POST.get("status")

        WardBed.objects.create(
            room_number=room_number,
            bed_number=bed_number,
            status=status
        )

        return redirect("room_list")
    return render(request,"departments/add_room.html")

def room_list(request):
    rooms=WardBed.objects.all()

    context={"rooms":rooms}

    return render(request,"departments/room_list.html",context)

def edit_room(request,id):
    edit = get_object_or_404(WardBed, id=id)

    if request.method == "POST":

        edit.room_number = request.POST.get("room_number")
        edit.bed_number = request.POST.get("bed_number")
        edit.status = request.POST.get("status")

        edit.save()

        return redirect("room_list")

    context = {
        "edit": edit
    }
    

    return render(request,"departments/edit_room.html",context)

def delete_room(request,id):
    delete_room=WardBed.objects.get(id=id)
    delete_room.delete()
    return redirect("room_list")

def Ward_Support_Staff(request):
    if request.method == "POST":

        name = request.POST.get("name")
        staff_type = request.POST.get("staff_type")
        phone = request.POST.get("phone")
        shift = request.POST.get("shift")
        status = request.POST.get("status")

        WardSupportStaff.objects.create(
            name=name,
            staff_type=staff_type,
            phone=phone,
            shift=shift,
            status=status
        )

        return redirect("suport_staff_list")
    return render(request,"departments/support_staff.html")


def Ward_Staff_list(request):

    person = WardSupportStaff.objects.all()

    context = {
        "person": person
    }

    return render(
        request,
        "departments/support_staff_list.html",
        context
    )

def edit_staff(request,id):
    edit=WardSupportStaff.objects.get(id=id)

    if request.method =="POST":
        edit.name=request.POST.get("name")
        edit.staff_type=request.POST.get("staff_type")
        edit.phone=request.POST.get("phone")
        edit.shift=request.POST.get("shift")
        edit.status=request.POST.get("status")
        edit.save()
        return redirect("suport_staff_list")

    context = {
        "edit": edit
    }

    return render(request,"departments/edit_staff.html",context)


def delete_staff(request,id):
    delete_staff=WardSupportStaff.objects.get(id=id)
    delete_staff.delete()
    return redirect("suport_staff_list")

def cardic_ward_dashboard(request):
    return render(request,"wards/cardic_dashboard.html")

def neuro_ward_dashboard(request):
    return render(request,"wards/neuro_dashboard.html")

def orthopedic_dasboard(request):
    return render(request,"wards/orthopedic_dashboard.html")

def childcare_dashbaord(request):
    return render(request,"wards/chilcare_dashboard.html")

def women_dashboard(request):
    return render(request,"wards/women_ward.html")

def gastro_ward(request):
    return render(request,"wards/gastro_ward.html")

def ent_eye_ward(request):
    return render(request,"wards/ent_eye_ward.html")

def skin_allery_ward(request):
    return render(request,"wards/skin_allergy_ward.html")

def surgery_ward(request):
    return render(request,"wards/surgery_emg_ward.html")



@login_required
def create_announcement(request):

    if request.method == "POST":

        Announcement.objects.create(
            title=request.POST.get("title"),
            message=request.POST.get("message"),
            recipient=request.POST.get("recipient"),
            priority=request.POST.get("priority"),
            attachment=request.FILES.get("attachment"),
            created_by=request.user
        )

        messages.success(
            request,
            "Announcement created successfully."
        )

        return redirect("announcemt_list")

    return render(request, "annoucemnt.html")


def annoucemnt_list(request):
    list=Announcement.objects.all()

    context={"list":list}

    return render(request,"annoucemt_list.html",context)

@login_required
def edit_announcement(request, id):

    announcement = Announcement.objects.get(id=id)

    if request.method == "POST":

        announcement.title = request.POST.get("title")
        announcement.message = request.POST.get("message")
        announcement.recipient = request.POST.get("recipient")
        announcement.priority = request.POST.get("priority")

        if request.FILES.get("attachment"):
            announcement.attachment = request.FILES.get("attachment")

        announcement.save()

        messages.success(
            request,
            "Announcement updated successfully."
        )

        return redirect("announcemt_list")

    return render(
        request,
        "edit_announcement.html",
        {"announcement": announcement}
    )

@login_required
def delete_announcement(request, id):

    announcement = Announcement.objects.get(id=id)

    announcement.delete()

    messages.success(
        request,
        "Announcement deleted successfully."
    )

    return redirect("announcemt_list")

#lab_technician Section
@login_required
def lab_home(request):
    
    list=register_data.objects.filter(role="lab_technician")
    reqt_list=ServiceRequest.objects.all()

   
  
    return render(request,"labtechnisian/lab_home.html",{"list":list,"user": request.user,"reqt_list":reqt_list})

@login_required
def upload_lab_report(request, request_id):

    reqt_list = get_object_or_404(ServiceRequest,id=request_id)

    if request.method == "POST":

        reqt_list.report_file = request.FILES.get("report_file")
        reqt_list.report_remarks = request.POST.get("report_remarks")

        reqt_list.save()
        return redirect("lab_home")



    return render(request, "labtechnisian/upload_report.html", {
            "reqt_list": reqt_list
    })