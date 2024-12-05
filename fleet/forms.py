from django import forms
from fleet.models import Fleet, Fleet_Log


class FleetForm(forms.ModelForm):
      def __init__(self, *args, **kwargs):
           super(FleetForm, self).__init__(*args, **kwargs)
           self.fields['start_date'].widget = forms.widgets.DateInput(
          
            attrs={
               'type': 'date',
                'class': 'form-control'
              
                
                
                }
            )
           self.fields['end_date'].widget = forms.widgets.DateInput(
          
            attrs={
               'type': 'date',
                'class': 'form-control'
              
                
                
                }
            )
        
           CHOICES1 =   (
            ('Vehicle', 'Vehicle'),
            ('MotorCycle', 'MotorCycle'),
     
             )
         
           CHOICES2 =   (
        ('Mercy Corps', 'Mercy Corps'),
        ('Rental', 'Rental'),
     
        )
       
        
        

       
           self.fields['vehicle_type'].widget = forms.widgets.Select(choices=CHOICES1)
           self.fields['ownership'].widget = forms.widgets.Select(choices=CHOICES2)
           self.fields['description'].widget = forms.widgets.Textarea(attrs={'type':'textarea', 'class': 'form-control', 'rows':'3', 'placeholder':'description'   }    )    
           myfield = ['tag_number',
            'field_office','vehicle_type',    
            'ownership',     

            ]
           for field in myfield:
                 self.fields[field].required = True 
      class Meta:
           model = Fleet
           fields = ['tag_number','field_office','vehicle_type','ownership', 'start_date','end_date','lin_code','vehicle_pic','chassis_number','description']
           exclude=  ['driver','supervisor']

class FleetLogForm(forms.ModelForm):
      def __init__(self, *args, **kwargs):
            super(FleetLogForm, self).__init__(*args, **kwargs)


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
        
            ('December', 'December'),
        
            )


            CHOICES2 =   (
            (2022, 2022),
            (2023, 2023),
            (2024, 2024),
            (2025, 2025),
            
            )

            self.fields['month_log'].widget = forms.widgets.Select(choices=CHOICES1)
            self.fields['year_log'].widget = forms.widgets.Select(choices=CHOICES2)

        
      class Meta:
            model = Fleet_Log
            fields = ['month_log','year_log','start_km','end_km','day_in_use','day_idle','day_in_workshop','workshop_visit','log_sheet']