import csv
import os
from program.models import Program 

from django.utils.formats import get_format
from collections import defaultdict

from django.db.models import Max, Avg,Sum, Count,Min
from easyaudit.models import RequestEvent, CRUDEvent, LoginEvent
from itertools import chain
import operator
def run():
    program_cn = Program.objects.annotate(num_cn=Count("icn__activity",distinct=True) + Count("icn",distinct=True)).order_by('-num_cn')
  
    for i in program_cn:
        print(i.title, i.num_cn)
    """
   qs1 = CRUDEvent.objects.filter(user_id=1).values('datetime__date').annotate(id_count=Count('id', distinct=True)).order_by("-datetime__date")
   qs2 = LoginEvent.objects.filter(user_id=1).values('datetime__date').annotate(count_login=Count('id', distinct=True)).order_by("-datetime__date")
   collector = defaultdict(dict)

   for collectible in chain(qs1, qs2):
      collector[collectible['datetime__date']].update(collectible.items())

   all_request = list(collector.values())
   
   for i in all_request:
      print(i)

      
  
   mcbt = 0
   for qs in qs:
      print(qs.mc_budget)
      if qs.mc_currency == 2:
         mcb = qs.mc_budget/120
      else:
         mcb = qs.mc_budget
      if qs.cs_currency == 2:
         csb = qs.cost_sharing_budget/120
      else:
         csb = qs.cost_sharing_budget
        

      mcbt= mcbt + mcb + csb
      
   if qs.icn.cs_currency == 2:
      imcb = qs.icn.mc_budget/120
   else:
      imcb = qs.icn.mc_budget

   if qs.icn.cs_currency == 2:
      icsb = qs.icn.cost_sharing_budget/120
   else:
      icsb = qs.icn.cost_sharing_budget

   itotalb = imcb + icsb
   remainb = itotalb - mcbt
   print(mcbt, qs.icn.mc_budget, remainb)
 
   #current_user = User.objects.filter(username='habtamu')
   #elig = UserRoles.objects.filter(program__in=program,is_pcn_initiator=True)
   #list1=list(elig)
   #if current_user in list1:
   #   print(current_user)
   #for u in userroles:
    #    print(u, u.program)
        
   

   program_cn = Program.objects.annotate(num_cn=Count("icn__activity") + Count("icn")).filter(num_cn__gte=1).order_by('-num_cn')

   for program in program_cn:
      print(program.title)
      print(program.num_cn)

   """