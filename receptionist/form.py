from django import forms
from .models import OPDRegistration

class OPDRegistrationForm(forms.ModelForm):

    class Meta:
        model = OPDRegistration
        fields = "__all__"