from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.db.models.functions import TruncMonth
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordResetView
# Create your views here.
from django.contrib.auth.decorators import login_required

from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
import json
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from core.models import User
from django.shortcuts import render, redirect
from core.models import User, Profile, FieldOffice
from fleet.models import *
import json
from django.db.models import Max, Avg,Sum,Count
from django.db.models import Q
from collections import defaultdict
from itertools import chain
from django import template
import requests
import pandas as pd



from datetime import datetime, timedelta
from django.utils import timezone
from datetime import datetime, date

from dateutil.relativedelta import relativedelta
from fleet.models import Fleet_Log, Fleet, Fleet_Expense, Generator, Generator_Report, Missing_Log, Missing_Expense
from fleet.forms import FleetForm, FleetLogForm, FleetLogFormEdit, FleetExpenseFormEdit, FleetExpenseForm, GeneratorForm, GeneratorReportForm, GeneratorReportFormEdit
from .forms import MissingLogForm



@login_required(login_url='login')
def missing_report(request):
    user = request.user
    form = MissingLogForm()

    user = request.user
    form = MissingLogForm()

    if user.is_superuser:
        fff = Missing_Log.objects.values('field_office').distinct()
        form.fields['field_office'].choices = [(ff.pk, ff.name) for ff in FieldOffice.objects.filter(id__in=fff).order_by('name')]
        form.fields['month'].choices =[(ff['month'], ff['month']) for ff in Missing_Log.objects.values('month').distinct()]
        form.fields['year'].choices =[(ff['year2'], ff['year2']) for ff in Missing_Log.objects.values('year2').distinct().order_by('-year2')]
    else:
  
        form.fields['field_office'].choices = [(ff.pk, ff) for ff in FieldOffice.objects.filter(id=user.profile.field_office.id)]
    
    context = {'form':form }
    
    

    
    return render(request, 'report/missing_report.html', context)


def get_report_form(request):
    user = request.user
    form = MissingLogForm()

    user = request.user
    form = MissingLogForm()

    if user.is_superuser:
        fff = Missing_Log.objects.values('field_office').distinct()
        form.fields['field_office'].choices = [(ff.pk, ff.name) for ff in FieldOffice.objects.filter(id__in=fff).order_by('name')]
        form.fields['month'].choices =[(ff['month'], ff['month']) for ff in Missing_Log.objects.values('month').distinct()]
        form.fields['year'].choices =[(ff['year2'], ff['year2']) for ff in Missing_Log.objects.values('year2').distinct().order_by('-year2')]
    else:
  
        form.fields['field_office'].choices = [(ff.pk, ff) for ff in FieldOffice.objects.filter(id=user.profile.field_office.id)]
    
    context = {'form':form }
    

   
    return render(request, 'report/partial/report_form.html', context)
    


@login_required(login_url='login')
def generate_report(request):
     
     if request.method == 'POST':
        
        month = request.POST.get("month")
        year = request.POST.get("year")
        field_office = request.POST.get("field_office")
        print(month)

        missing_report = Missing_Log.objects.filter(field_office=field_office, month=month, year2=year)
        missing_expense = Missed_Expense.objects.filter(field_office=field_office, month=month, year=year)
        qs1 = missing_expense.filter(fleet_id = None)
        qs2 = missing_expense.filter(ownership = 'Rental', rental_and_tax = '', rental_fees = '')
        qs3 = missing_expense.filter(ownership = 'Mercy Corps', rental_and_tax = '', tax_insurance = '')
        qs4 = missing_expense.filter(Q(fuel_cost = '' ) | Q(cost_labour = '') | Q(cost_consumables = None) | Q(cost_spares = '')).exclude(fleet_id = None)
   
        
        missing_expense = qs1.union(qs2, qs3, qs4).order_by('generate_series','id')
        total_missing = missing_report.count()
        total_expense = missing_expense.count()
        
        context = {'missing_report':missing_report, 'total_missing':total_missing, 'missing_expense':missing_expense, 'total_expense':total_expense}
       
            
    
        return render(request, 'report/partial/missing.html', context)
    
     return render(request, 'report/partial/missing.html')   
        

@login_required(login_url='login')
def aggregate_report(request):
    user = request.user
    if user.is_superuser:
        missing_log = Missing_Log.objects.all().order_by('generate_series','id')
    else:
        
        missing_log = Missing_Log.objects.filter(field_office_id=user.profile.field_office_id).order_by('field_office','id')
    
    context = {'missing_log':missing_log }
    
    
    return render(request, 'report/aggregate_report.html', context)



@login_required(login_url='login')
def dashboard(request):
    total_field_office  =  FieldOffice.objects.count
    total_fleet =  Fleet.objects.values('tag_number').distinct().count()
    total_fleet_mc=  Fleet.objects.filter(ownership='Mercy Corps',vehicle_type='Vehicle').values('tag_number').distinct().count()
    total_fleet_mc_m =  Fleet.objects.filter(ownership='Mercy Corps',vehicle_type='MotorCycle').values('tag_number').distinct().count()
    total_fleet_r =  Fleet.objects.filter(ownership='Rental').values('tag_number').distinct().count()
    
    total_user  =  Generator.objects.count
    
    ff_gens = FieldOffice.objects.annotate(num_gen=Count('generator')).order_by('-num_gen')[:7]
    ff_fleet = FieldOffice.objects.annotate(num_fleet=Count('assigned_to')).order_by('-num_fleet')
    ff_fleetr= FieldOffice.objects.filter(assigned_to__ownership ='Rental').annotate(num_fleet=Count('assigned_to')).order_by('-num_fleet')
    #program_cn = Program.objects.annotate(num_cn=Count("icn__activity",distinct=True) + Count("icn",distinct=True)).filter().order_by('-num_cn')[:12]
    ff_fleetmo= FieldOffice.objects.filter(assigned_to__vehicle_type ='MotorCycle').annotate(num_fleet=Count('assigned_to')).order_by('-num_fleet')
   
    context = {'total_field_office':total_field_office, 'total_fleet':total_fleet, 'total_fleet_mc':total_fleet_mc,
                'ff_fleetmo':ff_fleetmo,'ff_gens':ff_gens, 'ff_fleetr':ff_fleetr, 'total_fleet_r':total_fleet_r, 'total_user':total_user, 'ff_fleet':ff_fleet, 'total_fleet_mc_m':total_fleet_mc_m}
    
    return render(request, 'report/dashboard.html',context)


def years(request):
    form = MissingLogForm(request.GET)
    return HttpResponse(form['year'])

