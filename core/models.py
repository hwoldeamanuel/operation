from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Region(models.Model):
    
    name = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name

class Zone(models.Model):
    
    name = models.CharField(max_length=255, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Woreda(models.Model):
    
    name = models.CharField(max_length=255, unique=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class FieldOffice(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, null=True, blank=True)
    zone = models.ForeignKey(
        Zone, on_delete=models.CASCADE, null=True, blank=True)
    woreda = models.ForeignKey(
        Woreda, on_delete=models.CASCADE, null=True, blank=True)
    location_x = models.FloatField(null=True, blank=True)
    location_y = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name='profile')
    first_name = models.CharField(max_length=100,null=True, blank=True)
    last_name = models.CharField(max_length=100,null=True, blank=True)
    job_title =  models.CharField(max_length=100,null=True, blank=True)
    field_office = models.ForeignKey(FieldOffice, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='portfolio')
    contact_number = models.CharField(max_length=12, null=True, blank=True)
    reports_to = models.ForeignKey(
        User,
        related_name='supervisor',
       
        on_delete=models.DO_NOTHING,null=True, blank=True
    )
    

    def __str__(self):
        return self.user.username
    def full_name(self):
        return str(self.first_name) + " " + str(self.last_name)

