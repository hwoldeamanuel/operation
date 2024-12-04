from django.contrib import admin

# Register your models here.
from .models import Fleet, Fleet_Log


admin.site.register(Fleet)
admin.site.register(Fleet_Log)
