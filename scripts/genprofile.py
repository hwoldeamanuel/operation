import csv
import os
import requests
from django.db.models import Max, Avg,Sum, Count,Min

from django.db.models import Q
from itertools import chain
from collections import defaultdict
from django.db.models.functions import TruncMonth
from collections import defaultdict
import pandas as pd
from core.models import User, FieldOffice, Country, Region, Zone, Woreda
from fleet.models import Fleet, Fleet_Log, Fleet_Expense, Generator, Generator_Report


def run():
     
      total_fuel = Fleet_Expense.objects.filter(expense_type = 'Fuel cost').aggregate(Sum('expense_volume'))['expense_volume__sum']
      total_km   = Fleet_Log.objects.aggregate(Sum('km_driven'))['km_driven__sum']
      
      print(total_km)
      """ gens = Generator.objects.all()
      count = 1
      for record in read_file:
             
             if count == 1:
                         pass
             else:
                     gen = Generator.objects.get(id=record[0])
                     Generator_Report.objects.create(generator=gen, month_report=record[1], year_report=record[2], operated_time_hr = record[3],
                                                                     fuel_used_lt = record[4],  fuel_cost_br=record[5] , repair_cost_br=record[6])
                     print(gen)

                                          

                                    #if ff.name == record[5]:
                                    #print(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],)        
                     
                                    #Fleet.objects.create(tag_number = record[0], vehicle_type= record[1], chassis_number= record[2], 
                                                         #ownership=record[4], field_office=ff, start_date=record[11], end_date=record[12], lin_code=record[17])
                
             count = count + 1
	 """