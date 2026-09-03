from django.db import models

# Create your models here.
from django.db import models


class OPDRegistration(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    VISIT_TYPE = [
        ("New", "New"),
        ("Follow-up", "Follow-up"),
    ]

    PAYMENT_STATUS = [
        ("Paid", "Paid"),
        ("Unpaid", "Unpaid"),
    ]

    OPD_STATUS = [
        ("Waiting", "Waiting"),
        ("In Consultation", "In Consultation"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

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

    patient_id = models.CharField(max_length=20, unique=True)
    patient_name = models.CharField(max_length=100)
    department = models.CharField(max_length=50,choices=DEPARTMENT_CHOICES,blank=True,null=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile = models.CharField(max_length=10)
    address = models.TextField()

    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)

    visit_type = models.CharField(max_length=20, choices=VISIT_TYPE)

    symptoms = models.TextField(blank=True, null=True)

    registration_date = models.DateField(auto_now_add=True)

    registration_fee = models.DecimalField(max_digits=10, decimal_places=2)

    payment_status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS,
        default="Unpaid"
    )

    opd_status = models.CharField(
        max_length=20,
        choices=OPD_STATUS,
        default="Waiting"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient_id} - {self.patient_name}"


class Ambulance(models.Model):

    STATUS_CHOICES = [
        ("Available", "Available"),
        ("On Duty", "On Duty"),
        ("Maintenance", "Maintenance"),
    ]

    ambulance_no = models.CharField(max_length=20, unique=True)
    vehicle_name = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    driver_mobile = models.CharField(max_length=10)
    vehicle_type = models.CharField(max_length=50)
    purchase_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Available"
    )

    def __str__(self):
        return self.ambulance_no





class Visitor(models.Model):

    VISITOR_TYPE_CHOICES = [
        ("Patient Relative", "Patient Relative"),
        ("Patient Friend", "Patient Friend"),
        ("Doctor Visitor", "Doctor Visitor"),
        ("Medical Representative", "Medical Representative"),
        ("Vendor", "Vendor"),
        ("Delivery Person", "Delivery Person"),
        ("Maintenance Staff", "Maintenance Staff"),
        ("Government Official", "Government Official"),
        ("Job Applicant", "Job Applicant"),
        ("Other", "Other"),
    ]

    PURPOSE_CHOICES = [
        ("Meet Patient", "Meet Patient"),
        ("Meet Doctor", "Meet Doctor"),
        ("Medical Representative", "Medical Representative"),
        ("Equipment Delivery", "Equipment Delivery"),
        ("Maintenance Work", "Maintenance Work"),
        ("Interview", "Interview"),
        ("Submit Documents", "Submit Documents"),
        ("Collect Reports", "Collect Reports"),
        ("Administrative Work", "Administrative Work"),
        ("Other", "Other"),
    ]

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

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    STATUS_CHOICES = [
        ("Inside", "Inside"),
        ("Left", "Left"),
    ]

    visitor_id = models.AutoField(primary_key=True)

    visitor_name = models.CharField(max_length=100)

    mobile = models.CharField(max_length=10)

    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)

    visitor_type = models.CharField(max_length=30,choices=VISITOR_TYPE_CHOICES)

    purpose = models.CharField(max_length=30,choices=PURPOSE_CHOICES)

    patient_name = models.CharField(max_length=100,blank=True,null=True)

    doctor_name = models.CharField(max_length=100,blank=True,null=True)

    department = models.CharField(max_length=100,choices=DEPARTMENT_CHOICES)

    number_of_visitors = models.PositiveIntegerField(default=1)

    check_in = models.TimeField()

    check_out = models.TimeField(blank=True,null=True)

    visit_date = models.DateField(auto_now_add=True)

    remarks = models.TextField(blank=True,null=True)

    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default="Inside")

    def __str__(self):
        return f"{self.visitor_name} ({self.visitor_type})"


