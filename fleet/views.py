from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import FormView

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

import json
from django.db.models import Max, Avg,Sum,Count
from django.db.models import Q
from collections import defaultdict
from itertools import chain
from django import template



from datetime import datetime, timedelta
from django.utils import timezone
from datetime import datetime, date

from dateutil.relativedelta import relativedelta
from fleet.models import Fleet_Log, Fleet
from fleet.forms import FleetForm, FleetLogForm





def fleets(request):
    fleets = Fleet.objects.all().order_by('field_office','id')
    context = {'fleets':fleets }
    
    return render(request, 'fleet/fleets.html', context)

def fleet(request, id):
    fleet = get_object_or_404(Fleet,id=id)
    fleet_log = Fleet_Log.objects.filter(fleet=fleet).order_by('start_km')
    context = {'fleet':fleet, 'fleet_log':fleet_log }
    
    return render(request, 'fleet/fleet.html', context)

def fleet_list(request):
   
    fleets = Fleet.objects.all().order_by('field_office','id')
    context = {'fleets':fleets, }
    
    return render(request, 'fleet/partial/fleets_list.html', context)

def edit_fleet(request, id):
    fleet = Fleet.objects.get(pk=id)
    if request.method == "POST":
        form = FleetForm(request.POST, request.FILES, instance=fleet)
        if form.is_valid():
            instance =form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "FleetListChanged": None,
                        "showMessage": f"{instance.id} updated."
                    })
                }
            )
        else:
            form = FleetForm(instance=fleet)
            return render(request, 'fleet/partial/fleet_form.html', {
             'form': form,    'fleet': fleet,
            })

    else:
        form = FleetForm(instance=fleet)
    return render(request, 'fleet/partial/fleet_form.html', {
        'form': form,
        'fleet': fleet,
    })

def edit_fleet_log(request, id):
    fleet_log = Fleet_Log.objects.get(pk=id)
    if request.method == "POST":
        form = FleetLogForm(request.POST, request.FILES, instance=fleet_log)
        if form.is_valid():
            instance =form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "FleetListChanged": None,
                        "showMessage": f"{instance.id} updated."
                    })
                }
            )
    else:
        form = FleetLogForm(instance=fleet_log)
    return render(request, 'fleet/partial/fleetlog_form.html', {
        'form': form,
        'fleet_log': fleet_log,
    })


def add_fleet(request):
    
    form = FleetForm()
    if request.method == "POST":
        form = FleetForm(request.POST, request.FILES)
        if form.is_valid():
            
            instance = form.save()
            
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "FleetListChanged": None,
                         "showMessage": f"{instance.tag_number} updated."

                        
                    })
                }
            )
    else:
        form = FleetForm()
    return render(request, 'fleet/partial/fleet_form.html', {
        'form': form,
    })


def add_fleet_log(request, id):
    fleet = get_object_or_404(Fleet,id=id)
    form = FleetLogForm()
    if request.method == "POST":
        form = FleetLogForm(request.POST, request.FILES)
        if form.is_valid():
            
            instance = form.save(commit=False)
            instance.fleet = fleet
            instance.save()
            
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "FleetListChanged": None,
                         "showMessage": f"{instance.tag_number} updated."

                        
                    })
                }
            )
    else:
        form = FleetLogForm()
    return render(request, 'fleet/partial/fleetlog_form.html', {
        'form': form,
    })

def generators(request):
    return render(request, 'fleet/geneators.html')


def fieldoffice(request):
    return render(request, 'user/fieldoffice.html')



def fleet_filter(request):
    query = request.GET.get('search', '')
    
    
    
    if query:
        qs1 = Fleet.objects.filter(tag_number__icontains=query)
        qs2 = Fleet.objects.filter(field_office__name__icontains=query)
        qs3 = Fleet.objects.filter(ownership__icontains=query)
        qs4 = Fleet.objects.filter(vehicle_type__icontains=query)
        
        fleets = qs1.union(qs2, qs3, qs4).order_by('field_office','id')
       
        
    else:
        fleets = Fleet.objects.all()

    context = {'fleets': fleets}
    return render(request, 'fleet/partial/fleets_list.html', context)

def download_logsheet(request, id):
    log_sheet = get_object_or_404(Fleet_Log, id=id)
    response = HttpResponse(log_sheet.log_sheet, content_type='application/docx')
    response['Content-Disposition'] = f'attachment; filename="{log_sheet.log_sheet}"'
    return response