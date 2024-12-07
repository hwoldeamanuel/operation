import csv
import os
from fleet.models import Fleet, Fleet_Log, Fleet_Expense, Generator, Generator_Report
from datetime import datetime
import pandas as pd
from django.db.models.functions import TruncMonth
from django.db.models import Max, Avg,Sum, Count,Min

def run():
	gen = Generator.objects.get(id=1)
	x = Generator_Report.objects.filter(generator=gen).annotate(created_at_month=TruncMonth('report_start_date')).values('created_at_month').annotate(ops_hr=Sum('operated_time_hr')).annotate(cost_br=Sum('fuel_cost_br')).order_by('created_at_month')
	print(x)

    
	

"""  
      fleet = Fleet.objects.get(id=285)
      x = Fleet_Log.objects.filter(fleet=fleet).annotate(created_at_month=TruncMonth('log_start_date')).values('created_at_month').annotate(km_driven=Sum('km_driven')).order_by('created_at_month')
      y = Fleet_Expense.objects.filter(fleet=fleet).annotate(created_at_month=TruncMonth('expense_start_date')).values('created_at_month').annotate(total_expense=Sum('expense_value')).order_by('created_at_month')
      ydf = pd.DataFrame.from_dict(y)
      xdf = pd.DataFrame.from_dict(x)
   
      all_request = xdf.merge(ydf, how='outer')
      all_request['km_driven'] = all_request['km_driven'].fillna(0)
      all_request['total_expense'] = all_request['total_expense'].fillna(0)
      print(all_request)
      for a in all_request:
            print(a)
 
         
	expenses = Fleet_Expense.objects.all()
	for exp in expenses:
		if exp.month_expense and exp.year_expense:
			sd = datetime.strptime(exp.month_expense + ' 1 ' + str(exp.year_expense), '%B %d %Y')
			Fleet_Expense.objects.filter(id=exp.id).update(expense_start_date=sd)
            
	fleetlog = Fleet_Log.objects.all()
	for log in fleetlog:
		if log.log_start_date:
			ls = log.log_start_date + pd.DateOffset(months=1) - pd.DateOffset(days=1)
			df = ls.day
			
			print(ls, df)
	

	
	
	logs = Fleet_Log.objects.all()
	for log in logs:
		if log.start_km and log.end_km:
			kmd = (log.end_km - log.start_km)
			Fleet_Log.objects.filter(id=log.id).update(km_driven=kmd)

		#if log.year_log and log.month_log:
			#sd = datetime.strptime(log.month_log + ' 1 ' + str(log.year_log), '%B %d %Y')
			#Fleet_Log.objects.filter(id=log.id).update(log_start_date=sd)
		
			#print(log.log_start_date)
	

	

	file = open('C:/Users/Habtamu-MC/Desktop/ss.csv')
	read_file = csv.reader(file)
	for records in read_file:
		print(records)

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




    duser = []
    users = User.objects.all()
    
    for user in users:
        duser.append(user)
        
    print(duser)
	

gdps = Program.objects.annotate(user_cnt=Count('users_role'))

    # extract country names and GDPs
    for gdp in gdps:
    	print(gdp,gdp.user_cnt)
    
 file = open('C:/Users/Habtamu-MC/Desktop/IPTS/Woreda-Miss.csv')
	read_file = csv.reader(file)
	for records in read_file:
		for zone in Zone.objects.filter(id=1):
			Woreda.objects.create(id=records[1],name=records[0], zone=zone)
	for records in read_file:
   		for myregion in myregions:
			   if(myregion.name == records[1]):
							Woreda.objects.create(id=records[2],name=records[0], zone=myregion)
""" 
    
         
    
    
			    

