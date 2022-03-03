from django.forms import ModelForm, TextInput, DateInput,NumberInput

from .models import *


class LedgerForm(ModelForm):
    class Meta:
        model = Ledger
        fields = ['c_name', 'c_date_form_start', 'c_date_form_end', ]
        # fields =  '__all__'
        widgets = {
            'c_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'Enter Your Name',

            }),
            'c_date_form_start': DateInput(attrs={
                'type': 'date',
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'mm/dd/yyyy',
                'required': True,
            }),
            'c_date_form_end': DateInput(attrs={
                'type': 'date',
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'mm/dd/yyyy',
                'required': True,
            })

        }

class ledger_descriptionForm(ModelForm):
    class Meta:
        model = ledger_description
        print(model)
        fields = ['c_description', 'c_current_date', 'c_debt_amt', 'c_credit_amt', 'ledgerDetail', ]
        widgets = {
            'c_description': TextInput(attrs={
                'placeholder': 'Enter Your Description',
            }),

            'c_current_date': NumberInput(attrs={
                'type': 'date',
                'placeholder': 'mm/dd/yyyy',
            }),
            'c_debt_amt': NumberInput(attrs={
                'min':'0'
            }),
            'c_credit_amt': NumberInput(attrs={
                'min': '0'
            }),

        }



