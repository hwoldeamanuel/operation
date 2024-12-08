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
from fleet.models import Fleet_Log, Fleet, Fleet_Expense, Generator, Generator_Report
from fleet.forms import FleetForm, FleetLogForm, FleetLogFormEdit, FleetExpenseFormEdit, FleetExpenseForm, GeneratorForm, GeneratorReportForm, GeneratorReportFormEdit




@login_required(login_url='login')
def missing_report(request):
    
    
    return render(request, 'report/missing_report.html')

@login_required(login_url='login')
def aggregate_report(request):
    
    
    return render(request, 'report/aggregate_report.html')



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