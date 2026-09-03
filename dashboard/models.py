from django.db import models

# Create your models here.


class Appointment(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Rejected", "Rejected"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    appointment_id = models.CharField(max_length=20, blank=True, null=True)

    patient_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    phone = models.CharField(max_length=10)
    email = models.EmailField(blank=True, null=True)

    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100, blank=True, null=True)

    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    symptoms = models.TextField(blank=True, null=True)

    token_number = models.PositiveIntegerField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    remarks = models.TextField(blank=True, null=True)

    approved_by = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient_name