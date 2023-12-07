from django.db import models
from django.utils.translation import gettext_lazy as _


class FoodTruck(models.Model):

    class FacilityType(models.TextChoices):
        TRUCK = "TRUCK", _("Truck")
        PUSH_CART = "PCART", _("Push cart")
    
    class Status(models.TextChoices):
        APPROVED = "APPROVED", _("Approved")
        REQUESTED = "REQUESTED", _("Requested")
        SUSPEND = "SUSPEND", _("Suspend")
        EXPIRED = "EXPIRED", _("Expired")

    location_id = models.PositiveIntegerField()
    applicant = models.CharField(max_length=100)
    facility_type = models.CharField(max_length=5, choices=FacilityType.choices)
    cnn = models.PositiveIntegerField()
    location_description = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    block = models.CharField(max_length=5, null=True)
    lot = models.CharField(max_length=4, null=True)
    permit = models.CharField(max_length=11)
    status = models.CharField(max_length=9, choices=Status.choices)
    food_items = models.CharField(max_length=500, null=True)
    x = models.FloatField(null=True)
    y = models.FloatField(null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    schedule = models.CharField(max_length=200)
    dayshours = models.CharField(max_length=100)
    approved = models.DateTimeField(null=True)
    received = models.DateField()
    prior_permit = models.BooleanField()
    expiration_date = models.DateTimeField(null=True)
    fire_prevention_districts = models.PositiveSmallIntegerField(null=True)
    police_districts = models.PositiveSmallIntegerField(null=True)
    supervisor_districts = models.PositiveSmallIntegerField(null=True)
    zip_code = models.PositiveSmallIntegerField(null=True)
    neighborhoods_old = models.PositiveSmallIntegerField(null=True)
