import csv
import os
import datetime 
#import pandas as pd
from django.contrib.auth.models import User
from app_admin.models import Country,Region, Zone,Woreda, Portfolio_Type, Portfolio_Category
from django.shortcuts import get_object_or_404
from program.models import Program
from django.db.models import Max, Avg,Sum,Count
from dateutil.parser import parserinfo, parser, parse

def run():
	file = open('C:/Users/Habtamu-MC/Desktop/IPTS/programlist.csv')
	read_file = csv.reader(file)
	Program.objects.all().delete()

	count = 1
	
	for record in read_file:
		if count == 1:
			pass
		else:
			
			# Example usage
			date_string1 = record[4]
			result_datetime1 = convert_to_datetime(date_string1)
			date_string2 = record[4]
			result_datetime2= convert_to_datetime(date_string2)
		
 
			
			Program.objects.create(title = record[0], description = record[1], donor = record[2],
								fund_code = record[3], start_date = result_datetime1 , end_date = result_datetime2)
		
			
		count = count + 1
		


def convert_to_datetime(input_str, parserinfo=None):
	return parse(input_str, parserinfo=parserinfo)