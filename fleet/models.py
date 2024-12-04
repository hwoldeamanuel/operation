from django.db import models

# Create your models here.
from core.models import FieldOffice
from core.models import Profile

class Fleet(models.Model):
    field_office = models.ForeignKey(FieldOffice, on_delete= models.DO_NOTHING, null=True,  blank=True, related_name='assigned_to')
    tag_number = models.CharField(max_length = 255, null=True, blank=True)
    vehicle_type = models.CharField(max_length = 255, null=True, blank=True)
    chassis_number = models.CharField(max_length = 255, null=True, blank=True)
    year_make = models.CharField(max_length = 255, null=True, blank=True)
    ownership = models.CharField(max_length = 255, null=True, blank=True)
    driver = models.ForeignKey(Profile, on_delete= models.DO_NOTHING, null=True,  blank=True, related_name='driver')
    supervisor = models.ManyToManyField(Profile,  blank=True, related_name='supervisors')
    make = models.CharField(max_length = 255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    lin_code =  models.CharField(max_length = 255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,  null=True,  blank=True)
    modified_at = models.DateTimeField(auto_now_add=True,  null=True,  blank=True)

    vehicle_pic = models.ImageField(upload_to ='documents/', null=True, blank=True) 

    class Meta:
        unique_together = ('field_office', 'tag_number')
    
    def __str__(self):
        return str(self.id)


class Fleet_Log(models.Model):
    fleet = models.ForeignKey(Fleet, on_delete= models.DO_NOTHING, null=True,  blank=True, related_name='assigned_to')
    tag_number = models.CharField(max_length = 255, null=True, blank=True)
    field_office = models.ForeignKey(FieldOffice,on_delete= models.DO_NOTHING, null=True, blank=True)
    month_log =  models.CharField(max_length = 255, null=True, blank=True)
    year_log =  models.IntegerField(null=True, blank=True)
    start_km = models.FloatField(null=True, blank=True)
    end_km = models.FloatField(null=True, blank=True)
    day_in_use = models.IntegerField(null=True, blank=True)
    day_idle = models.IntegerField(null=True, blank=True)
    day_in_workshop = models.IntegerField(null=True, blank=True)
    workshop_visit = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.tag_number


