from django.forms import ModelForm, TextInput, DateInput, NumberInput
from django import forms
import datetime
from .models import *
from django.core.exceptions import NON_FIELD_ERRORS

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
        fields = ['c_description', 'c_current_date', 'c_debt_amt', 'c_credit_amt', ]
        widgets = {
            'c_description': TextInput(attrs={
                'placeholder': 'Enter Your Description',
                'class': 'rounded border-success',
            }),

            'c_current_date': DateInput(attrs={
                'type': 'date',
                'placeholder': 'mm/dd/yyyy',
                'class': 'rounded border-primary',
            }),
            'c_debt_amt': NumberInput(attrs={
                'class': 'rounded border-secondary',
                'min': '0'
            }),
            'c_credit_amt': NumberInput(attrs={
                'class': 'rounded border-warning',
                'min': '0'
            }),

        }


PAYMENT_CHOICES = (
    ("1", "Cash"),
    ("2", "Credit"),
    ("3", "Card"),
)


class CustomerForm(forms.ModelForm):
    date_time = forms.DateTimeField(initial=datetime.datetime.now, disabled=True)
    class Meta:
        model = Customer

        fields = [
            'customer_name',
            'address',
            'phone',
            'pan_no',
            'invoice_no',
            'invoice_date',
            'payment_mode',
            'subtotal',
            'discount',
            'taxable_amount',
            'vat',
            'total_amount',
            'in_words',
            'remarks',
            'received_by',
            'prepared_by',
            'authorized_sign',
        ]

        widgets = {
            'customer_name': forms.TextInput(attrs={'style': 'width: 220px;' 'height: 30px;'}),
            'address': forms.TextInput(attrs={'style': 'width: 220px;' 'height: 30px;'}),
            'phone': forms.TextInput(attrs={'style': 'width: 220px;' 'height: 30px;'}),
            'pan_no': forms.TextInput(attrs={'style': 'width: 220px;' 'height: 30px;'}),
            'invoice_no': forms.TextInput(attrs={'placeholder': 'Enter Unique No','style': 'width: 160px;' 'height: 30px;'}),
            'invoice_date': forms.DateInput(attrs={'type': 'date', 'style': 'width: 160px;' 'height: 30px;'}),
            'payment_mode': forms.Select(choices=PAYMENT_CHOICES),
            'subtotal': forms.NumberInput(attrs={'style': 'width: 150px;' 'height: 30px;'}),
            'discount': forms.NumberInput(attrs={'style': 'width: 150px;' 'height: 30px;'}),
            'taxable_amount': forms.NumberInput(attrs={'readonly':'readonly','style': 'width: 150px;' 'height: 30px;'}),
            'vat': forms.NumberInput(attrs={'readonly':'readonly','style': 'width: 150px;' 'height: 30px;'}),
            'total_amount': forms.NumberInput(attrs={'readonly':'readonly','style': 'width: 150px;' 'height: 30px;'}),
            'in_words': forms.TextInput(attrs={'style': 'width: 500px;' 'height: 30px;'}),
            'remarks': forms.Textarea(attrs={'style': 'width: 500px;' 'height: 30px;'}),
            'received_by': forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;'}),
            'prepared_by': forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;'}),
            'authorized_sign': forms.TextInput(
                attrs={'style': 'width: 180px;' 'height: 30px;'}),
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Bill

        fields = [
            'item_no',
            'particular',
            'alt_qty',
            'quantity',
            'Uom',
            'rate',
            'discount',
            'amount',
        ]

        widgets = {
            'item_no': forms.TextInput(attrs={'class': 'formset-field','style': 'width: 50px;' 'height: 30px;'}),
            'particular': forms.Textarea(attrs={'class': 'formset-field', 'style': 'width: 250px;' 'height: 30px;'}),
            'alt_qty': forms.TextInput(attrs={'class': 'formset-field', 'style': 'width: 80px;' 'height: 30px;'}),
            'quantity': forms.TextInput(attrs={'class': 'formset-field', 'style': 'width: 80px;' 'height: 30px;'}),
            'Uom': forms.TextInput(attrs={'class': 'formset-field', 'style': 'width: 70px;' 'height: 30px;'}),
            'rate': forms.NumberInput(attrs={'class': 'formset-field', 'style': 'width: 110px;' 'height: 30px;'}),
            'discount': forms.NumberInput(attrs={'class': 'formset-field', 'style': 'width: 110px;' 'height: 30px;'}),
            'amount': forms.NumberInput(attrs={'class': 'formset-field', 'readonly':'readonly', 'style': 'width: 110px;' 'height: 30px;'}),
        }


