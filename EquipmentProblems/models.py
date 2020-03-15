from django.db import models
from django.db.models import Model
from django.db.models import (
    IntegerField,
    CharField,
    BooleanField,
    TextField,
    DateField,
    TimeField,
    OneToOneField,
)


class EquipementName(Model):
    name = TextField()

class EquipementSystem(Model):
    name = TextField()

class ProblemType(Model):
    name = TextField()

class NITTECEmployee(Model):
    name = TextField()

class ReportingName(Model):
    name = TextField()

class ReportingMemberAgency(Model):
    name = TextField()

class PhoneNumber(Model):
    name = TextField()

class TicketNumber(Model):
    name = TextField()

class OwningAgency(Model):
    name = TextField()

class OutsideSupport(Model):
    name = TextField()

class EquipementProblemsTable(Model):
    report_id = IntegerField()

    start_date = DateField()
    start_time = TimeField()
    end_date = DateField()
    end_time = DateField()

    status = BooleanField()

    OPERATIONAL_STATUS_CHOICES = (
        ('OOS', 'Out of Service' ),
        ('NM', 'Needs Maintenance'),
    )
    Operational_Status = CharField(max_length = 120, choices = OPERATIONAL_STATUS_CHOICES)

    Description = TextField()
    NotifOutside_Support = TextField()
    System_Staff_Action = TextField()

    Website_CCTV_Off_date = DateField()
    Website_CCTV_On_date = DateField()
    Website_CCTV_Off_time = TimeField()
    Website_CCTV_Off_time = TimeField()

    

    NITTEC_Employee = OneToOneField(NITTECEmployee,null=True, on_delete=models.SET_NULL)
    Reporting_Name = OneToOneField(ReportingName, null=True, on_delete=models.SET_NULL)
    Reporting_Member_Agency = OneToOneField(ReportingMemberAgency, null=True, on_delete=models.SET_NULL)
    Phone_number = OneToOneField(PhoneNumber, null=True, on_delete=models.SET_NULL)
    Ticket_number = OneToOneField(TicketNumber, null=True, on_delete=models.SET_NULL)

    Equipement_name = OneToOneField(EquipementName, null=True, on_delete=models.SET_NULL)
    Affected_system = OneToOneField(EquipementSystem, null=True, on_delete=models.SET_NULL)
    Problem_type = OneToOneField(ProblemType, null=True, on_delete=models.SET_NULL)
    Owning_agency = OneToOneField(OwningAgency, null=True, on_delete=models.SET_NULL)
    Outside_support = OneToOneField(OutsideSupport, null=True, on_delete=models.SET_NULL)


