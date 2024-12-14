
import csv
import os

import datetime 
from django.utils.formats import get_format


from django.db.models import Max, Avg,Sum, Count,Min
from easyaudit.models import RequestEvent, CRUDEvent, LoginEvent
import json


from django.db.models import F    
from django.contrib.auth.models import Group, Permission, User

from django.shortcuts import get_object_or_404
from collections import defaultdict
from itertools import chain
from django import template

from django.db.models import Q
from django.db import models
from django.db.models.functions import TruncMonth 

from datetime import datetime, timedelta
register = template.Library()
import datetime
from django.utils import timezone
from fleet.models import Test, Missing_Log, Missing_Expense, Missed_Expense
from core.models import FieldOffice
from fleet.models import *
from itertools import chain
from operator import attrgetter
import pandas as pd

def run():
    
    ffs =  Log_Report.objects.annotate(created_at_month=TruncMonth('log_start_date')).values('created_at_month').annotate(day_total=Sum('day_total')).annotate(day_use=Sum('day_use')).annotate(day_available=Sum('day_available')).order_by('created_at_month')
    fdf = pd.DataFrame.from_dict(ffs)
    fdf['usage'] = fdf['day_use'] / fdf['day_total'] *100
    fdf['avalablity'] = fdf['day_available'] / fdf['day_total'] *100

    
    print(fdf)
    """
    field_office = 9
    ff_fleet1 =  FieldOffice.objects.filter(assigned_to__vehicle_type ='Vehicle').annotate(num_vfleet=Count('assigned_to')).values('name','num_vfleet').order_by('-num_vfleet')
    ff_fleet2 = FieldOffice.objects.filter(assigned_to__vehicle_type ='MotorCycle').annotate(num_mfleet=Count('assigned_to')).values('name','num_mfleet').order_by('-num_mfleet')
    ffdf = pd.DataFrame.from_dict(ff_fleet1)
    ggdf = pd.DataFrame.from_dict(ff_fleet2)
    ff_fleet = ffdf.merge(ggdf,  how="left", on="name", indicator=True)
    ff_fleet['num_vfleet'] = ff_fleet['num_vfleet'].fillna(0)
    
    ff_fleet['num_mfleet'] = ff_fleet['num_mfleet'].fillna(0)
    ff_fleet['num_mfleet'] = ff_fleet['num_mfleet'].astype(int)
    ff_fleet['total'] = ff_fleet['num_vfleet'] + ff_fleet['num_mfleet']   
    ff_fleet.sort_values(by=['total'], ascending=False)
    print(ff_fleet)   
   
  """