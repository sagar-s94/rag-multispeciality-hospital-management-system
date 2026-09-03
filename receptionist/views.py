from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from dashboard.models import Appointment
from .models import OPDRegistration
from .models import Ambulance
from .models import Visitor
from django.db.models import Q
from django.contrib import messages
from doctor.models import ServiceRequest




# Create your views here.
def recep_home(request):
    
    return render(request,"recep_home.html")

def appoint_list(request):
    appointments=Appointment.objects.all()

    name = request.GET.get("patient_name")
    date = request.GET.get("appointment_date")

    if name:
        appointments = appointments.filter(patient_name__icontains=name)

    if date:
        appointments = appointments.filter(appointment_date=date)

   
    context = {
        "appointments": appointments
    }
    return render(request,"appoint_list.html",context)


def add_opd(request):

    if request.method == "POST":

        patient_id = request.POST.get("patient_id")
        patient_name = request.POST.get("patient_name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        department = request.POST.get("department")
        doctor = request.POST.get("doctor")
        visit_type = request.POST.get("visit_type")
        symptoms = request.POST.get("symptoms")
        registration_fee = request.POST.get("registration_fee")
        payment_status = request.POST.get("payment_status")
        opd_status = request.POST.get("opd_status")

        OPDRegistration.objects.create(
            patient_id=patient_id,
            patient_name=patient_name,
            age=age,
            gender=gender,
            mobile=mobile,
            address=address,
            department=department,
            doctor=doctor,
            visit_type=visit_type,
            symptoms=symptoms,
            registration_fee=registration_fee,
            payment_status=payment_status,
            opd_status=opd_status,
        )

        return redirect("opd_list")


    return render(request,"patients/addopd.html")

def opd_list(request):
    opds=OPDRegistration.objects.all()

    context={
        "opds":opds
    }
    return render(request,"patients/opd_list.html",context)

def Update_opd(request):
    opd_data=OPDRegistration.objects.all()

    search=request.GET.get("search")

    if search:
        opd_data=OPDRegistration.objects.filter(Q(patient_id__icontains=search) |
                                                Q(patient_name__icontains=search) |
                                                Q(age__icontains=search) |
                                                Q(gender__icontains=search) |
                                                Q(mobile__icontains=search) |
                                                Q(address__icontains=search) |
                                                Q(department__icontains=search) |
                                                Q(doctor__icontains=search) |
                                                Q(visit_type__icontains=search) |
                                                Q(symptoms__icontains=search) |
                                                Q(registration_fee__icontains=search) |
                                                Q(payment_status__icontains=search) |
                                                Q(opd_status__icontains=search))
        if opd_data.exists():
            messages.success(request, "Record found successfully.")
        else:
            messages.error(request, "Record not found.")

    context={"opd_data":opd_data}

    return render(request,"patients/update_opd.html",context)



def edit_opd(request,id):
    edit=OPDRegistration.objects.get(id=id)
    if request.method =="POST":
            edit.patient_name = request.POST.get("patient_name")
            edit.age = request.POST.get("age")
            edit.gender = request.POST.get("gender")
            edit.mobile = request.POST.get("mobile")
            edit.address = request.POST.get("address")
            edit.department = request.POST.get("department")
            edit.doctor = request.POST.get("doctor")
            edit.visit_type = request.POST.get("visit_type")
            edit.symptoms = request.POST.get("symptoms")
            edit.registration_fee = request.POST.get("registration_fee")
            edit.payment_status = request.POST.get("payment_status")
            edit.opd_status = request.POST.get("opd_status")

            edit.save()

            return redirect("updateopd")


    return render(request,"patients/edit_opd.html",{"edit":edit})


def generate_invoice(request, patient_id):
    opd = OPDRegistration.objects.get(patient_id=patient_id)

    return render(
        request,
        "report/genrate_invoice.html",
        {"patient": opd}
    )

def delete_opd(request,patient_id):
    patient = get_object_or_404(OPDRegistration, patient_id=patient_id)
    patient.delete()
    return redirect("opd_list") 

def add_ambulance(request):
    if request.method == "POST":
        ambulance_no=request.POST.get("ambulance_no")
        vehicle_name=request.POST.get("vehicle_name")
        
        driver_name=request.POST.get("driver_name")
        driver_mobile=request.POST.get("driver_mobile")
        vehicle_type=request.POST.get("vehicle_type")
        purchase_date=request.POST.get("purchase_date")
        status=request.POST.get("status")

        Ambulance.objects.create(
            ambulance_no=ambulance_no,
            vehicle_name=vehicle_name,
            
            driver_name=driver_name,
            driver_mobile=driver_mobile,
            vehicle_type=vehicle_type,
            purchase_date=purchase_date,
            status=status,

        )
        messages.success(request, "Ambulance added successfully.")
        return redirect("add_ambulance")


    return render (request,"ambulance/add_ambu.html")

def ambulance_list(request):

    search = request.GET.get("search")

    ambulance = Ambulance.objects.all()

    if search:
        ambulance = ambulance.filter(
            ambulance_no__icontains=search
        )

    return render(request,"ambulance/abmulance_list.html",{"ambulance": ambulance},)

def delete_ambulance(request,id):
    data=get_object_or_404(Ambulance,id=id)
    data.delete()
    return redirect ("ambulance_list")

def add_visitor(request):

    if request.method == "POST":

        Visitor.objects.create(

            visitor_name=request.POST.get("visitor_name"),
            mobile=request.POST.get("mobile"),
            gender=request.POST.get("gender"),
            visitor_type=request.POST.get("visitor_type"),
            purpose=request.POST.get("purpose"),
            patient_name=request.POST.get("patient_name"),
            doctor_name=request.POST.get("doctor_name"),
            department=request.POST.get("department"),
            number_of_visitors=request.POST.get("number_of_visitors"),
            check_in=request.POST.get("check_in"),
            check_out=request.POST.get("check_out") or None,
            remarks=request.POST.get("remarks"),
            status=request.POST.get("status"),
        )

        return redirect("visitor_list")

    return render(request, "vistors/add_vistors.html")

def visitor_list(request):

    search = request.GET.get("search", "")
    status = request.GET.get("status", "")

    visitors = Visitor.objects.all().order_by("-visit_date")

    if search:

        visitors = visitors.filter(
            Q(visitor_name__icontains=search) |
            Q(mobile__icontains=search) |
            Q(visitor_type__icontains=search) |
            Q(patient_name__icontains=search) |
            Q(doctor_name__icontains=search)
        )

    if status:

        visitors = visitors.filter(status=status)

    context = {
        "visitors": visitors,
        "search": search,
        "status": status,
    }

    return render(request, "vistors/visitor_list.html", context)


def edit_visitor(request, visitor_id):

    visitor = get_object_or_404(
        Visitor,
        visitor_id=visitor_id
    )

    if request.method == "POST":

        visitor.visitor_name = request.POST.get("visitor_name")
        visitor.mobile = request.POST.get("mobile")
        visitor.gender = request.POST.get("gender")
        visitor.visitor_type = request.POST.get("visitor_type")
        visitor.purpose = request.POST.get("purpose")
        visitor.patient_name = request.POST.get("patient_name")
        visitor.doctor_name = request.POST.get("doctor_name")
        visitor.department = request.POST.get("department")
        visitor.number_of_visitors = request.POST.get("number_of_visitors")
        visitor.check_in = request.POST.get("check_in")
        visitor.check_out = request.POST.get("check_out") or None
        visitor.remarks = request.POST.get("remarks")
        visitor.status = request.POST.get("status")

        visitor.save()

        return redirect("visitor_list")

    return render(
        request,
        "vistors/edit_visitor.html",
        {"visitor": visitor}
    )


def delete_visitor(request, visitor_id):

    visitor = get_object_or_404(
        Visitor,
        visitor_id=visitor_id
    )

    visitor.delete()

    return redirect("visitor_list")

def service_slip(request, id):

    service = ServiceRequest.objects.get(id=id)

    context = {
        "service": service
    }

    return render(request,"service_slip.html",context)

