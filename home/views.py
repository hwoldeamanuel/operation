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
    
    
    return render(request, 'report/dashboard.html')