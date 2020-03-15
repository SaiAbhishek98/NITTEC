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
from GeneralEvents.models import Operators, CallerDetails


class DamageClaim(Model):
    Caller_details = OneToOneField(CallerDetails, null = True, on_delete=models.SET_NULL)
    Address = TextField()
    City = TextField()
    State = TextField()
    ZipCode = IntegerField()
    
    NYSDOT_Claims = BooleanField()
    NYSTA = BooleanField()
    Eerie_County = BooleanField()

    Vehicle_information = TextField()
    Other = TextField()

class GeneralInformation(Model):
    slug = TextField() 

class DamageClaimTable(Model):
    report_id = IntegerField()

    Operator = OneToOneField(Operators, null=True, on_delete=models.SET_NULL)

    Date = DateField()
    Time = TimeField()

    TYPE_CHOICES = (
        ('DC', 'Damage Claim' ),
        ('Info', 'General Information'),
    )
    Type = CharField(max_length = 120, choices = TYPE_CHOICES)


    Damage_claim = OneToOneField(DamageClaim, null=True, on_delete=models.SET_NULL)
    General_information = OneToOneField(GeneralInformation, null = True, on_delete=models.SET_NULL)






