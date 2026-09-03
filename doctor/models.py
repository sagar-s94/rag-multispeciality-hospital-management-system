from django.db import models

from hospitaladmin.models import General_IPDPatient
from accounts.models import register_data


# Create your models here.
class ServiceRequest(models.Model):

    SERVICE_CHOICES = (
        ('ecg', 'ECG'),
        ('blood_test', 'Blood Test'),
        ('xray', 'X-Ray'),
        ('ct_scan', 'CT Scan'),
        ('mri', 'MRI'),
        ('ultrasound', 'Ultrasound'),
        ('echo', 'Echocardiography'),
        ('eeg', 'EEG'),
        ('other', 'Other'),
    )

    PRIORITY_CHOICES = (
        ('normal', 'Normal'),
        ('urgent', 'Urgent'),
        ('emergency', 'Emergency'),
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    doctor = models.ForeignKey(
        register_data,
        on_delete=models.CASCADE,
        related_name='doctor_requests'
    )

    patient = models.ForeignKey(
        General_IPDPatient,
        on_delete=models.CASCADE,
        related_name='patient_requests'
    )

    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='normal'
    )

    instructions = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    report_file = models.FileField(
        upload_to="lab_reports/",
        blank=True,
        null=True
    )

    report_remarks = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.patient} - {self.get_service_display()}"