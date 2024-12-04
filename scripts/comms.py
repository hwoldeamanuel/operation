from commcare_export.checkpoint import CheckpointManagerWithDetails
from commcare_export.commcare_hq_client import CommCareHqClient, AUTH_MODE_APIKEY
from commcare_export.commcare_minilinq import get_paginator, PaginationMode

username = 'hwoldeamanuel@mercycorps.org'
domain = 'mc-ethiopia'
hq_host = 'https://commcarehq.org'
API_KEY= '6fec…9e02'

api_client = CommCareHqClient(hq_host, domain, username, API_KEY, AUTH_MODE_APIKEY)
case_paginator=get_paginator(resource='case', pagination_mode=PaginationMode.date_modified)
case_paginator.init()
checkpoint_manager=CheckpointManagerWithDetails(None, None, PaginationMode.date_modified)

cases = api_client.iterate('case', case_paginator, checkpoint_manager=checkpoint_manager)

for case in cases:
	print(case['case_id'])