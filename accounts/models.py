from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser



class register_data(AbstractUser):

    ROLE_CHOICES = (
       ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('receptionist', 'Receptionist'),
        ('ward_receptionist', 'Ward Receptionist'),
        ('nurse', 'Nurse'),
        ('lab_technician', 'Lab Technician'),
        ('pharmacist', 'Pharmacist'),
        ('accountant', 'Accountant'),
        ('patient', 'Patient'),

    )
    DEPARTMENT_CHOICES = (
        ('general', 'General'),
        ('cardiac', 'Cardiac'),
        ('neuro', 'Neuro'),
        ('orthopedic', 'Orthopedic'),
        ('child_care', 'Child Care'),
        ('women_maternity', 'Women & Maternity'),
        ('gastro_kidney', 'Gastro & Kidney'),
        ('ent_eye', 'ENT & Eye'),
        ('skin_allergy', 'Skin & Allergy'),
        ('surgery_emergency', 'Surgery & Emergency'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    department = models.CharField(max_length=50,choices=DEPARTMENT_CHOICES,blank=True,null=True)

    phone = models.CharField(max_length=15, unique=True)

    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)

    address = models.TextField(blank=True)

    def __str__(self):
        return self.username