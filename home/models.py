# models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, empcode, empname, password=None, **extra_fields):
        if not empcode:
            raise ValueError('The employee code field must be set')
        user = self.model(empcode=empcode, empname=empname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, empcode, empname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(empcode, empname, password, **extra_fields)

class ConcreteUser(AbstractBaseUser, PermissionsMixin):
    EMPLOYEE_STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]
    
    GENDER_CHOICES = [
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
    ]
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    empcode = models.CharField(max_length=10, unique=True)
    empname = models.CharField(max_length=50)
    designation = models.CharField(max_length=50, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=128)
    rolename = models.CharField(max_length=50)
    createdby = models.CharField(max_length=50)
    jn_date = models.DateField(null=True, blank=True)
    lv_date = models.DateField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    mail_id = models.EmailField(max_length=50, null=True, blank=True)
    external_mail = models.EmailField(max_length=50, null=True, blank=True)
    personal_mail = models.EmailField(max_length=50, null=True, blank=True)
    mail_indi = models.CharField(max_length=50, null=True, blank=True)
    gndr = models.IntegerField(choices=GENDER_CHOICES, default=1)
    QMS = models.BooleanField(default=True)
    SAP = models.BooleanField(default=True)
    crnt_sts = models.IntegerField(choices=EMPLOYEE_STATUS_CHOICES, default=1)
    mgr = models.CharField(max_length=50, null=True, blank=True)
    blood_group = models.CharField(max_length=10, null=True, blank=True)
    phno = models.CharField(max_length=15, null=True, blank=True)
    loc = models.CharField(max_length=50, null=True, blank=True)
    empgroup = models.CharField(max_length=20, null=True, blank=True)
    empsubgroup = models.CharField(max_length=20, null=True, blank=True)
    payscale_grade = models.CharField(max_length=20, null=True, blank=True)
    payscale_level = models.CharField(max_length=20, null=True, blank=True)
    payscale_sub_level = models.CharField(max_length=20, null=True, blank=True)
    pay_range = models.CharField(max_length=20, null=True, blank=True)
    adapt = models.CharField(max_length=20, null=True, blank=True)
    empType = models.CharField(max_length=50, null=True, blank=True)
    extn = models.CharField(max_length=50, null=True, blank=True)
    shrt = models.CharField(max_length=50, null=True, blank=True)
    active_name = models.CharField(max_length=10, null=True, blank=True)
    photo_sts = models.BooleanField(default=False)
    build_no = models.CharField(max_length=10, null=True, blank=True)
    room_no = models.CharField(max_length=10, null=True, blank=True)
    local_std_code = models.CharField(max_length=10, null=True, blank=True)
    sys_no = models.CharField(max_length=15, null=True, blank=True)
    loc_outstn = models.CharField(max_length=50, null=True, blank=True)
    gl = models.CharField(max_length=60, null=True, blank=True)
    tl = models.CharField(max_length=50, null=True, blank=True)
    level_1 = models.CharField(max_length=50, null=True, blank=True)
    level_2 = models.CharField(max_length=50, null=True, blank=True)
    company_id = models.CharField(max_length=50, null=True, blank=True)
    tprog = models.CharField(max_length=20, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    delete1 = models.BooleanField(default=False)
    marital_status = models.IntegerField(choices=[(0, 'Single'), (1, 'Married')], default=0)
    tms_status = models.BooleanField(default=False)
    ass_role = models.CharField(max_length=10, null=True, blank=True)
    qualification = models.CharField(max_length=20, default='SSC', null=True, blank=True)
    empcode_md5 = models.CharField(max_length=50, null=True, blank=True)
    tr_facility = models.CharField(max_length=10, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    marriage_date = models.DateField(null=True, blank=True)
    phone_permission = models.CharField(max_length=20, default='0')
    bus_route = models.CharField(max_length=10, null=True, blank=True, default='0')
    ext_status = models.CharField(max_length=10, null=True, blank=True)
    work_loc = models.CharField(max_length=50, null=True, blank=True)
    audit_emp_sts = models.CharField(max_length=50, null=True, blank=True)
    auditor_qua_date = models.DateField(null=True, blank=True)
    auditor_disqua_date = models.DateField(null=True, blank=True)
    uan = models.CharField(max_length=20, null=True, blank=True)
    pan = models.CharField(max_length=20, null=True, blank=True)
    bank_indi = models.CharField(max_length=500, null=True, blank=True)
    bank_acc = models.CharField(max_length=500, null=True, blank=True)
    attendance_status = models.CharField(max_length=10, null=True, blank=True)
    ess = models.CharField(max_length=10, null=True, blank=True)
    alt_contact = models.CharField(max_length=20, null=True, blank=True)
    ot_flag = models.CharField(max_length=20, null=True, blank=True)
    rsc = models.CharField(max_length=2, null=True, blank=True)
    emp_cat = models.CharField(max_length=20, null=True, blank=True)

    USERNAME_FIELD = 'empcode'
    REQUIRED_FIELDS = ['empname']

    objects = UserManager()

    def __str__(self):
        return self.empname

    class Meta:
        db_table = 'user_master'
        verbose_name = 'user'
        verbose_name_plural = 'users'
