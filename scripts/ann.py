
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
from conceptnote.models import Icn, IcnSubmit, ActivitySubmit
from datetime import datetime, timedelta
register = template.Library()
import datetime
from django.utils import timezone

def run():
    icn = Icn.objects.values('approval_status').annotate(icn_count=Count('id', distinct=True))
         
     
    
    
    print(icn)
  