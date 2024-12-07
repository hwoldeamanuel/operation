from django.db import models

# Create your models here.
from core.models import FieldOffice
from core.models import Profile
from datetime import datetime

class Fleet(models.Model):
    field_office = models.ForeignKey(FieldOffice, on_delete= models.DO_NOTHING, null=True,  blank=True, related_name='assigned_to')
    tag_number = models.CharField(max_length = 255, null=True, blank=True)
    vehicle_type = models.CharField(max_length = 255, null=True, blank=True)
    chassis_number = models.CharField(max_length = 255, null=True, blank=True)
    year_make = models.CharField(max_length = 255, null=True, blank=True)
    ownership = models.CharField(max_length = 255, null=True, blank=True)
    driver = models.CharField(max_length = 255, null=True, blank=True)
    
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
        return self.tag_number


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
    log_sheet = models.FileField(null=True,  blank=True, upload_to='documents/')
    log_start_date = models.DateField(null=True, blank=True)
    km_driven = models.FloatField(null=True, blank=True)


    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        self.log_start_date = datetime.strptime(self.month_log + ' 1 ' + str(self.year_log), '%B %d %Y')
        self.km_driven = self.end_km - self.start_km
        super(Fleet_Log, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


class Fleet_Expense(models.Model):
    fleet = models.ForeignKey(Fleet, on_delete= models.DO_NOTHING, null=True,  blank=True, related_name='assign_to')
    tag_number = models.CharField(max_length = 255, null=True, blank=True)
    field_office = models.ForeignKey(FieldOffice,on_delete= models.DO_NOTHING, null=True, blank=True)
    month_expense =  models.CharField(max_length = 255, null=True, blank=True)
    year_expense =  models.IntegerField(null=True, blank=True)
    expense_type =  models.CharField( max_length=255, null=True, blank=True)
    expense_volume = models.FloatField(null=True, blank=True)
    expense_value = models.FloatField(null=True, blank=True)
    volume_unit =  models.CharField(max_length = 255, null=True, blank=True)
    expense_start_date = models.DateField(null=True, blank=True)


   

    def __str__(self):
        return str(self.id)
   
class Generator(models.Model):
    field_office = models.ForeignKey(FieldOffice,on_delete= models.DO_NOTHING, null=True, blank=True)
    title =  models.CharField(max_length = 255, null=True, blank=True)
    make =  models.CharField(max_length = 255, null=True, blank=True)
    hour_liter =  models.FloatField(null=True, blank=True)
    person_in_charge =  models.CharField(max_length = 255, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    old_id =  models.IntegerField(null=True, blank=True)
    generator_pic = models.ImageField(upload_to ='documents/', null=True, blank=True) 

    def __str__(self):
        return str(self.id)

class Generator_Report(models.Model):
    generator= models.ForeignKey(Generator,on_delete= models.DO_NOTHING, null=True, blank=True)
    month_report =  models.CharField(max_length = 255, null=True, blank=True)
    year_report =  models.IntegerField(null=True, blank=True)
    operated_time_hr =  models.FloatField(null=True, blank=True)
    fuel_used_lt = models.FloatField(null=True, blank=True)
    fuel_cost_br = models.FloatField(null=True, blank=True)
    repair_cost_br = models.FloatField(null=True, blank=True)
    report_start_date = models.DateField(null=True, blank=True)

    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        self.report_start_date = datetime.strptime(self.month_report + ' 1 ' + str(self.year_report), '%B %d %Y')
        super(Generator_Report, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)




