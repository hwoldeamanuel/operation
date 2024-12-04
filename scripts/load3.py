import csv
import os
from program.models import Program 
import datetime 
from django.utils.formats import get_format


from django.db.models import Max, Avg,Sum, Count,Min
from easyaudit.models import RequestEvent, CRUDEvent, LoginEvent
import json
from django import template
from conceptnote.models import Icn, Impact
from program.models import Indicator, UserRoles, Program
from itertools import chain
from user.models import Profile
from django.db.models import F    
from django.contrib.auth.models import Group, Permission, User

from django.shortcuts import get_object_or_404
from collections import defaultdict
from itertools import chain
from django import template
from conceptnote.models import Icn, Activity, IcnImplementationArea
from django.db.models import Q
from django.db import models
from django.db.models.functions import TruncMonth 
from report.models import IcnReport, ActivityReport, IcnReportImpact, ActivityImpact, ActivityReportImpact
from conceptnote.models import Icn, IcnSubmit
from datetime import datetime, timedelta
register = template.Library()
import datetime
from django.utils import timezone

def run():
    last_month_filter = timezone.now() - timedelta(days=get_lapse())
    print(last_month_filter)
    user_activity = CRUDEvent.objects.filter(datetime__gte=last_month_filter).order_by('-id')
    for act in user_activity:
        print(act.datetime)
      #suffix = f"{q.pk}".zfill(4)
      #icn_number = f"{q.program.title}/ICN/{suffix}"   
      #Icn.objects.filter(pk=q.id).update(icn_number=icn_number)
    #s1 = Icn.objects.filter(program_id = pk).annotate(m=TruncMonth('created')).values("m").annotate(icn_count=Count('id', distinct=True))
    #qs2 = Activity.objects.filter(program_id = id).annotate(m=TruncMonth('created')).values("m").annotate(activity_count=Count('id', distinct=True))
 
def get_lapse():
    last_month = timezone.now().month
    current_year = timezone.now().year

    #is last month a month with 30 days?
    if last_month in [9, 4, 6, 11]:
        lapse = 30

    #is last month a month with 31 days?
    elif last_month in [1, 3, 5, 7, 8, 10, 12]:
        lapse = 31

    #is last month February?
    else:
        if is_leap_year(current_year):
            lapse = 29
        else:
            lapse = 30

    return lapse
 


    #collector = defaultdict(dict)

    #for collectible in chain(qs1, qs2):
     #   collector[collectible['m']].update(collectible.items())
    

"""
qs1 = Icn.objects.filter(ilead_agency_id = 1).annotate(m=TruncMonth('created')).values("m").annotate(icn_count=Count('id', distinct=True))
    qs2 = Activity.objects.filter(alead_agency_id = 1).annotate(m=TruncMonth('created')).values("m").annotate(activity_count=Count('id', distinct=True))
 



    collector = defaultdict(dict)

    for collectible in chain(qs1, qs2):
        collector[collectible['m']].update(collectible.items())

    all_request = list(collector.values())
    
    print(all_request)
user = User.objects.filter(username='hwoldeamanuel')
     userroles = UserRoles.objects.filter(user__in=user)
     qsi = Icn.objects.filter(Q(user__in=user) | Q(program_lead__in=userroles) | Q(technical_lead__in=userroles)| Q(finance_lead__in=userroles)).only("title", "id","user","program_lead","technical_lead","finance_lead","status","approval_status")
     qsa = Activity.objects.filter(Q(user__in=user) | Q(program_lead__in=userroles) | Q(technical_lead__in=userroles)| Q(finance_lead__in=userroles)).only("title", "id", "user","program_lead","technical_lead","finance_lead","status","approval_status")
    
     
     
     qs = list(chain(qsi, qsa))
     #questionnaire.objects.filter(test_population__user=user)
     #program_users = Program.objects.annotate(num_user=Count("users_role")).order_by('-num_user')[:12]
     for i in qs:
        
        print(i.finance_lead)
    

    user_activity = CRUDEvent.objects.filter(user=1).order_by('-id')[:12]
    for item in  user_activity:
        item.object_json_repr = jsonify(item.object_json_repr)
    qs1 = RequestEvent.objects.filter(user_id=1).values('datetime__date').annotate(id_count=Count('id', distinct=True))
    qs2 = RequestEvent.objects.filter(user_id=1, method='POST').values('datetime__date').annotate(count_login=Count('id', distinct=True))
    collector = defaultdict(dict)

    for collectible in chain(qs1, qs2):
        collector[collectible['datetime__date']].update(collectible.items())

    all_request = list(collector.values()) 
    for request in all_request:
        print(request)
    
@register.filter(name='jsonify')
def jsonify(data):
    if isinstance(data, dict):
        return data
    else:
        return json.loads(data)



    collector = defaultdict(dict)

    for collectible in chain(qs1, qs2):
        collector[collectible['datetime__date']].update(collectible.items())

    all_request = list(collector.values()) 
     
	

	rma =RequestEvent.objects.filter(user_id=1).values('datetime__date').annotate(id_count=Count('id', distinct=True))
	login_activity = LoginEvent.objects.filter(user_id=1).values('datetime__date').annotate(count_login=Count('id', distinct=True))
	qs = list(chain(rma,login_activity))
	for r in qs:
		print(r)
	#start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
	#end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d')

	#print("Number of weeks from",start_date_str,"to",end_date_str)

	#for date in (start_date + datetime.timedelta(n) for n in range((end_date - start_date).days + 1)):
		#week_num = date.isocalendar()[1]
		#print(date.strftime('%Y-%m-%d'),"is in week number",week_num)



    qs = Impact.objects.filter(icn_id=1).annotate(Count('indicators', distinct=True))
    
        
	  
    print(qs[0].indicators__count)
            


@register.filter(name='jsonify')
def jsonify(data):
    if isinstance(data, dict):
        return data
    else:
        return json.loads(data)

  labels = []
  data = []
  gdp = GDP.objects.values('country').annotate(agdp=Avg('gdp')).annotate(sgdp=Sum('gdp')).order_by('-agdp')
  for item in gdp:
    print(item)

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
"""