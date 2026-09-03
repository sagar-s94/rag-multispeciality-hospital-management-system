from django.shortcuts import render,redirect
from .models import Appointment
from django.contrib import messages
from receptionist.models import Ambulance
# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html")

def appointments(request):
    if request.method == "POST":

        
        patient_name=request.POST.get("patient_name")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        department=request.POST.get("department")
        doctor=request.POST.get("doctor")
        appointment_date=request.POST.get("appointment_date")
        appointment_time=request.POST.get("appointment_time")
        symptoms=request.POST.get("symptoms")
        

        Appointment.objects.create(
        patient_name=patient_name,
        age=age,
        gender=gender,
        phone=phone,
        email=email,
        department=department,
        doctor=doctor,
        appointment_date=appointment_date,
        appointment_time=appointment_time,
        symptoms=symptoms,
        )
        messages.success(request, "Your appointment has been booked successfully!")
        return redirect("dashboard")

    return render (request,"appointments.html")

def list_ambulance(request):
    search = request.GET.get("search")
    
    ambulance = Ambulance.objects.all()
    
    if search:
        ambulance = ambulance.filter(ambulance_no__icontains=search)
    
    return render(request,"ambulance_list.html",{"ambulance": ambulance})