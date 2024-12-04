
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
from fleet.models import Fleet, Fleet_Log


def run():
      
      file = open('C:/Users/Habtamu-MC/Desktop/IPTS/log.csv')
      read_file = csv.reader(file)
      fleet = Fleet.objects.all()
      fos = FieldOffice.objects.all()
      count = 1
      for record in read_file:
             if count == 1:
                         pass
             else:
                     for ff in fleet:
                             for fo in fos:
                                     if ff.tag_number == record[0] and fo.name == record[9]:
                                             Fleet_Log.objects.create(fleet=ff, tag_number=record[0], field_office=fo, month_log=record[1], year_log=record[2], start_km=record[3], end_km=record[4],
                                                                  day_in_use=record[6],	day_idle=record[7],	day_in_workshop=record[8], workshop_visit=record[12])

                                          

                                    #if ff.name == record[5]:
                                    #print(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],)        
                     
                                    #Fleet.objects.create(tag_number = record[0], vehicle_type= record[1], chassis_number= record[2], 
                                                         #ownership=record[4], field_office=ff, start_date=record[11], end_date=record[12], lin_code=record[17])
                
             count = count + 1
	

  
