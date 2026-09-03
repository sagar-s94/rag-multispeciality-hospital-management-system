from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from receptionist.models import OPDRegistration
from hospitaladmin.models import General_IPDPatient
from .models import ServiceRequest
from django.contrib.auth import logout
from receptionist.models import Visitor


# Create your views here.
def docotr_dashboard(request):
    doctor = request.user


    

   
    return render(request,"doctor_dashboard.html",{"doctor": doctor})


def doctor_logout(request):
    logout(request)
    return redirect("login_form")


@login_required
def profile(request):
    doctor = request.user
    return render(request,"profile.html", {"doctor": doctor})


@login_required
def edit_profile(request):
    edit = request.user
    if request.method == "POST":

        edit.first_name = request.POST.get("first_name")
        edit.last_name = request.POST.get("last_name")
        edit.email = request.POST.get("email")
        edit.phone = request.POST.get("phone")
        edit.department = request.POST.get("department")
        edit.address = request.POST.get("address")

        if request.FILES.get("profile_image"):
            edit.profile_image = request.FILES.get("profile_image")

        edit.save()

        return redirect("doctor_profile")

    context = {
        "edit": edit
    }

    return render(request,"edit_profile.html",context)



    



def ipd_patient_list(request):
    
    ipd_list=General_IPDPatient.objects.filter(department=request.user.department)
    search=request.GET.get("search")
    if search:
        ipd_list=ipd_list.filter(patient_name__icontains=search)

    context={"ipd_list":ipd_list,
             "search": search,}

    return render(request,"ipd_list.html",context)

@login_required
def make_request(request):
    # Only doctors can make service requests
    if request.user.role != "doctor":
        return redirect("doctor_dashboard")


    # Get only IPD patients from doctor's department
    patients = General_IPDPatient.objects.filter(
        department=request.user.department
    )


    if request.method == "POST":

        patient_id = request.POST.get("patient")
        service = request.POST.get("service")
        priority = request.POST.get("priority")
        instructions = request.POST.get("instructions")


        # Check patient selection
        if not patient_id:

            return render(
                request,
                "make_request.html",
                {
                    "patients": patients,
                    "error": "Please select a patient."
                }
            )


        # Get selected patient
        patient = get_object_or_404(
            General_IPDPatient,
            id=patient_id,
            department=request.user.department
        )


        # Create request
        ServiceRequest.objects.create(

            doctor=request.user,

            patient=patient,

            service=service,

            priority=priority,

            instructions=instructions

        )


        return redirect("request_list")


    context = {
        "patients": patients
    }

    return render (request,"make_request.html",context)



def request_list(request):
    search = request.GET.get("search")
    request=ServiceRequest.objects.all()

    if search:
        request = request.filter(
            service__icontains=search
        )
    context={"request":request}
    return render(request,"request_list.html",context)

def request_edit(request, id):

    edit = ServiceRequest.objects.get(id=id)

    if request.method == "POST":

        edit.service = request.POST.get("service")
        edit.priority = request.POST.get("priority")
        edit.status = request.POST.get("status")

        edit.save()

        return redirect("request_list")

    context = {
        "edit": edit
    }

    return render(request, "edit_list.html", context)

def delete_request(request,id):
    delet=ServiceRequest.objects.get(id=id)
    delet.delete()
    return redirect("request_list")

def department_visitors(request, department):

    visitors = Visitor.objects.filter(department=department)

    context = {
        "visitors": visitors,
        "department": department
    }

    return render(request,"dept_vistor_list.html",context)

