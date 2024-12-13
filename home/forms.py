

from django import forms
from core.models import FieldOffice
from fleet.models import Missing_Log

#(icn.pk, icn) for icn in Icn.objects.filter(id=icn.id)
CHOICES1 =   (
           
            ('January', 'January'),
            ('February', 'February'),
            ('March', 'March'),
            ('April', 'April'),
            ('May', 'May'),
            ('June', 'June'),
            ('July', 'July'),
            ('August', 'August'),
            ('September', 'September'),
            ('October', 'October'),
        
            ('November', 'November'),
        
            ('December', 'December')
        
            )


CHOICES2 =   (
           
            (2023, 2023),
            (2024, 2024),
            (2025, 2025)
            )

class MissingLogForm(forms.Form):
      field_office = forms.ChoiceField( required=False)
      month = forms.ChoiceField()
      year = forms.ChoiceField()

      def __init__(self, *args, **kwargs):
            super(MissingLogForm, self).__init__(*args, **kwargs)
            self.fields['month'].required = True 
            self.fields['year'].required = True 


    
     

