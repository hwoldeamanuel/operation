
import csv
import os
from fleet.models import Fleet, Fleet_Log, Fleet_Expense, Generator, Generator_Report
from datetime import datetime
import pandas as pd
from django.db.models.functions import TruncMonth
from django.db.models import Max, Avg,Sum, Count,Min
from core.models import User 
from dateutil.relativedelta import relativedelta
from datetime import date

def run():
    
    def date_list():
       
        mydate = datetime.now()
        mn = mydate.strftime("%B")
        yn = mydate.strftime("%Y")
        td = datetime.strptime(mn + ' 1 ' + str(yn), '%B %d %Y')
        td = td.date()

        ed =  date(2023,7,1)
       
      
        
        start_date = ed
       


        start_date = start_date.replace(day=1)


        
        
        end_date = td
       
        date_list = []

        curr_date = start_date
        while curr_date < end_date:
             date_list.append(curr_date)
             curr_date = curr_date + relativedelta(months=1)
            
        return date_list
    

    #start_date =  datetime.strptime('December' + ' 1 ' + str(2023), '%B %d %Y')
    #stop_date = start_date+ relativedelta(months=1)
    #date_list = date_range_list(start_date, stop_date)
    
    d = date_list()
   
    df = pd.DataFrame(d, columns=['months'], index=[0])

    
    df['Fuel cost'] = 'Fuel cost'
    df['Rental fees, Tax, insurance, miscs'] = 'Rental fees, Tax, insurance, miscs'
    df['Cost of labour'] = 'Cost of labour'
    df['Cost of Spares'] = 'Cost of Spares'
    df['Rental fees'] = 'Rental fees'
    df['Tax, Insurance, miscs'] = 'Tax, Insurance, miscs'
    
    
    fleet = Fleet.objects.all().values('id')
    dff = pd.DataFrame(columns=['fleet','months','Fuel cost','Rental fees, Tax, insurance, miscs','Cost of labour','Cost of Spares','Rental fees','Tax, Insurance, miscs'], index=[0])
    for fl in fleet:
        ydf = pd.DataFrame.from_dict(fl)
        df1 = df.join(ydf, how='outer')
        print(df1)
        #dff = dff.append(df1)
 
    #print(dff)
   

    
    #y = Fleet_Expense.objects.filter(fleet=fleet.id).annotate(created_at_month=TruncMonth('expense_start_date')).values('created_at_month').annotate(total_expense=Sum('expense_value')).order_by('created_at_month')
    #ydf = pd.DataFrame.from_dict(y)
   

   
    """
     expenses = Fleet_Expense.objects.filter(expense_start_date = None)
    for exp in expenses:
          if exp.year_expense and exp.month_expense:
               sd = datetime.strptime(exp.month_expense + ' 1 ' + str(exp.year_expense), '%B %d %Y')
               Fleet_Expense.objects.filter(id=exp.id).update(expense_start_date=sd)
               print(exp.expense_start_date)
        
    """
   