
import csv
import os
from fleet.models import Fleet, Fleet_Log, Fleet_Expense, Generator, Generator_Report
from datetime import datetime
import pandas as pd
from django.db.models.functions import TruncMonth
from django.db.models import Max, Avg,Sum, Count,Min
from core.models import User 

def run():
    expenses = Fleet_Expense.objects.filter(expense_start_date = None)
    for exp in expenses:
          if exp.year_expense and exp.month_expense:
               sd = datetime.strptime(exp.month_expense + ' 1 ' + str(exp.year_expense), '%B %d %Y')
               Fleet_Expense.objects.filter(id=exp.id).update(expense_start_date=sd)
               print(exp.expense_start_date)