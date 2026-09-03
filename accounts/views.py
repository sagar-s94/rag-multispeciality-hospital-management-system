from django.shortcuts import render, redirect
from .forms import userRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout

# Create your views here.


def register(request):

    form = userRegisterForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("login_form")

    return render(request, "registerform.html", {
        "form": form
    })

def login_form(request):

    form = AuthenticationForm()

    if request.method == "POST":

        form = AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.role == "admin":
                return redirect("Admin_home")

            elif user.role == "doctor":
                return redirect("dr_dashboard")

            elif user.role == "receptionist":
                return redirect("recep_home")

            elif user.role == "ward_receptionist":
                return redirect("ward_dashboard")

            elif user.role == "nurse":
                return redirect("nurse_dashboard")

            elif user.role == "lab_technician":
                return redirect("lab_home")

            elif user.role == "pharmacist":
                return redirect("pharmacy_dashboard")

            elif user.role == "patient":
                return redirect("patient_dashboard")

            else:
                form = AuthenticationForm()


    return render(request,"login.html",{"form":form})

def user_logout(request):
    logout(request)

    return redirect("login_form")
