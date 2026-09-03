from django.db import models
from django.conf import settings

# Create your models here.
class Doctor(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    doctor_id = models.AutoField(primary_key=True)

    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )
    date_of_birth = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(
        upload_to="doctors/",
        null=True,
        blank=True
    )

    # Professional Information
    specialization = models.CharField(max_length=150)
    department = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    experience = models.PositiveIntegerField(default=0)
    registration_no = models.CharField(
        max_length=100,
        unique=True
    )
    joining_date = models.DateField()

    # Contact Information
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    # Hospital Information
    room_no = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    available_days = models.CharField(
        max_length=100,
        blank=True
    )

    start_time = models.TimeField(
        null=True,
        blank=True
    )

    end_time = models.TimeField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active"
    )

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"




class Nurse(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    QUALIFICATION_CHOICES = [
        ("ANM", "ANM"),
        ("GNM", "GNM"),
        ("B.Sc Nursing", "B.Sc Nursing"),
        ("M.Sc Nursing", "M.Sc Nursing"),
    ]

    DESIGNATION_CHOICES = [
        ("Staff Nurse", "Staff Nurse"),
        ("Senior Staff Nurse", "Senior Staff Nurse"),
        ("Nursing Supervisor", "Nursing Supervisor"),
        ("Head Nurse", "Head Nurse"),
    ]

    SHIFT_CHOICES = [
        ("Morning", "Morning"),
        ("Evening", "Evening"),
        ("Night", "Night"),
        ("Rotational", "Rotational"),
    ]

    EMPLOYMENT_CHOICES = [
        ("Full Time", "Full Time"),
        ("Part Time", "Part Time"),
        ("Contract", "Contract"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("On Leave", "On Leave"),
        ("Inactive", "Inactive"),
    ]

 
  

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES
    )

    date_of_birth = models.DateField()

    profile_image = models.ImageField(
        upload_to="nurses/",
        blank=True,
        null=True
    )

  
    # Professional Information
 

    registration_no = models.CharField(
        max_length=100,
        unique=True
    )

    qualification = models.CharField(
        max_length=50,
        choices=QUALIFICATION_CHOICES
    )

    specialization = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    experience = models.PositiveIntegerField(
        default=0
    )

    designation = models.CharField(
        max_length=100,
        choices=DESIGNATION_CHOICES
    )

    joining_date = models.DateField()

  
    # Hospital Assignment


    department = models.CharField(
        max_length=150
    )

    ward = models.CharField(
        max_length=150
    )

    room_no = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    shift = models.CharField(
        max_length=50,
        choices=SHIFT_CHOICES
    )

    start_time = models.TimeField(
        blank=True,
        null=True
    )

    end_time = models.TimeField(
        blank=True,
        null=True
    )

    employment_type = models.CharField(
        max_length=50,
        choices=EMPLOYMENT_CHOICES
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Active"
    )

    # Contact Information
    #

    phone = models.CharField(
        max_length=15
    )

    email = models.EmailField()

    address = models.TextField(
        blank=True,
        null=True
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    state = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    pincode = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    
    # Timestamps
    

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"





class General_IPDPatient(models.Model):

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

    # Patient Information
    ipd_number = models.CharField(max_length=30, unique=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)

    gender = models.CharField(max_length=20)

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    age = models.PositiveIntegerField()

    blood_group = models.CharField(
        max_length=5,
        blank=True
    )

    phone = models.CharField(max_length=15)

    address = models.TextField()

    city = models.CharField(
        max_length=100,
        blank=True
    )

    department = models.CharField(max_length=50,choices=DEPARTMENT_CHOICES,blank=True,null=True)

    # Admission Information
    admission_date = models.DateField()
    admission_time = models.TimeField()

    admission_type = models.CharField(
        max_length=20,
        choices=[
            ("Emergency", "Emergency"),
            ("Routine", "Routine"),
            ("Referral", "Referral"),
        ],
        default="Routine"
    )

    doctor = models.CharField(
        max_length=100
    )

    ward = models.CharField(
        max_length=100,
       
    )

    room_no = models.CharField(
        max_length=20
    )

    bed_no = models.CharField(
        max_length=20
    )

    referred_by = models.CharField(
        max_length=100,
        blank=True
    )

    # Medical Information
    chief_complaint = models.TextField()

    symptoms = models.TextField(
        blank=True
    )

    diagnosis = models.TextField(
        blank=True
    )

    allergies = models.TextField(
        blank=True
    )

    medical_history = models.TextField(
        blank=True
    )

    current_medication = models.TextField(
        blank=True
    )

    patient_condition = models.CharField(
        max_length=20,
        choices=[
            ("Stable", "Stable"),
            ("Serious", "Serious"),
            ("Critical", "Critical"),
        ],
        default="Stable"
    )

    # Emergency Contact
    emergency_contact_name = models.CharField(
        max_length=100
    )

    emergency_contact_relation = models.CharField(
        max_length=50
    )

    emergency_contact_phone = models.CharField(
        max_length=15
    )

    # Billing
    payment_type = models.CharField(
        max_length=30,
        choices=[
            ("Cash", "Cash"),
            ("Insurance", "Insurance"),
            ("Government Scheme", "Government Scheme"),
        ],
        default="Cash"
    )

    insurance_company = models.CharField(
        max_length=150,
        blank=True
    )

    policy_number = models.CharField(
        max_length=100,
        blank=True
    )

    # IPD Status
    status = models.CharField(
        max_length=20,
        choices=[
            ("Admitted", "Admitted"),
            ("Discharged", "Discharged"),
            ("Transferred", "Transferred"),
        ],
        default="Admitted"
    )

    expected_discharge_date = models.DateField(
        null=True,
        blank=True
    )

    discharge_date = models.DateField(
        null=True,
        blank=True
    )

    discharge_notes = models.TextField(
        blank=True
    )

    # System Information
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.ipd_number} - {self.first_name} {self.last_name}"





class WardBed(models.Model):

    BED_STATUS = [
        ("available", "Available"),
        ("occupied", "Occupied"),
        ("maintenance", "Maintenance"),
    ]

    room_number = models.CharField(max_length=20)

    bed_number = models.CharField(max_length=20)

    patient = models.ForeignKey(
        "General_IPDPatient",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="ward_beds"
    )

    status = models.CharField(
        max_length=20,
        choices=BED_STATUS,
        default="available"
    )

    def __str__(self):
        return f"Room {self.room_number} - Bed {self.bed_number}"


class WardSupportStaff(models.Model):

    STAFF_TYPE = [
        ("ward_boy", "Ward Boy"),
        ("cleaning", "Cleaning Worker"),
        ("housekeeping", "Housekeeping"),
        ("attendant", "Attendant"),
        ("security", "Security"),
        ("other", "Other"),
    ]

    SHIFT_CHOICES = [
        ("morning", "Morning"),
        ("evening", "Evening"),
        ("night", "Night"),
        ("rotational", "Rotational"),
    ]

    STATUS_CHOICES = [
        ("active", "Active"),
        ("on_leave", "On Leave"),
        ("inactive", "Inactive"),
    ]

    name = models.CharField(max_length=100)
    staff_type = models.CharField(
        max_length=30,
        choices=STAFF_TYPE
    )
    phone = models.CharField(max_length=15)
    shift = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active"
    )

    def __str__(self):
        return self.name


class Announcement(models.Model):

    ROLE_CHOICES = [
        ("doctor", "Doctor"),
        ("nurse", "Nurse"),
        ("receptionist", "Receptionist"),
        ("ward_receptionist", "Ward Receptionist"),
        ("hostel_staff", "Hostel Staff"),
    ]

    PRIORITY_CHOICES = [
        ("normal", "Normal"),
        ("important", "Important"),
        ("urgent", "Urgent"),
    ]

    title = models.CharField(max_length=200)

    message = models.TextField()

    recipient = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="normal"
    )

    attachment = models.FileField(
        upload_to="announcements/",
        blank=True,
        null=True
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title