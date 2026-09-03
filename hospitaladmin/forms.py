from django import forms
from .models import Doctor
from .models import Nurse


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor

        fields = [
            "first_name",
            "last_name",
            "gender",
            "date_of_birth",
            "profile_image",

            "specialization",
            "department",
            "qualification",
            "experience",
            "registration_no",
            "joining_date",

            "phone",
            "email",
            "address",
            "city",
            "state",
            "pincode",

            "room_no",
            "consultation_fee",
            "available_days",
            "status",
            "start_time",
            "end_time",
        ]

       
class NurseForm(forms.ModelForm):

    class Meta:
        model = Nurse

        fields = [
            "first_name",
            "last_name",
            "gender",
            "date_of_birth",
            "profile_image",

            "registration_no",
            "qualification",
            "specialization",
            "experience",
            "designation",
            "joining_date",

            "department",
            "ward",
            "room_no",
            "shift",
            "start_time",
            "end_time",
            "employment_type",
            "status",

            "city",
            "state",
            "pincode",
            ]
    