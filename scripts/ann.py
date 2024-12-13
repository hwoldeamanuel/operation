
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

def run():
    field_office = 9
    month = 'November'
    year = 2024
    qs1 = Missed_Expense.objects.filter(fleet_id = None)
    qs2 = Missed_Expense.objects.filter(ownership = 'Rental', rental_and_tax = '', rental_fees = '')
    qs3 = Missed_Expense.objects.filter(ownership = 'Mercy Corps', rental_and_tax = '', tax_insurance = '')
    qs4 = Missed_Expense.objects.filter(Q(fuel_cost = '' ) | Q(cost_labour = '') | Q(cost_consumables = None) | Q(cost_spares = '')).exclude(fleet_id = None)
   
        
    missing_expense = qs1.union(qs2, qs3, qs4).order_by('generate_series','id')
       
    print(qs1.count()) 
    print(qs2.count())   
    print(qs3.count())   
    print(qs4.count())  
    print(missing_expense.count())      
   
  