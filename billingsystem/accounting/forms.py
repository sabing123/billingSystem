from django.forms import ModelForm, TextInput, DateInput, NumberInput
from django import forms
import datetime
from .models import *

PAYMENT_CHOICES = (
    ("1", "Cash"),
    ("2", "Credit"),
    ("3", "Card"),
)


class CustomerForm(forms.Form):
    customer_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'style': 'width: 220px;' 'height: 30px;', 'class': 'form-control'}))
    address = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'style': 'width: 220px;' 'height: 30px;', 'class': 'form-control'}))
    phone = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'style': 'width: 220px;' 'height: 30px;', 'class': 'form-control'}))
    pan_no = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'style': 'width: 220px;' 'height: 30px;', 'class': 'form-control'}))
    invoice_no = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'style': 'width: 160px;' 'height: 30px;', 'class': 'form-control'}))
    invoice_date = forms.DateField(initial=datetime.date.today, widget=forms.NumberInput(
        attrs={'type': 'date', 'style': 'width: 160px;' 'height: 30px;', 'class': 'form-control'}))
    payment_mode = forms.ChoiceField(choices=PAYMENT_CHOICES)


class ItemForm(forms.Form):
    item_no = forms.CharField(
        widget=forms.TextInput(attrs={'style': 'width: 50px;' 'height: 30px;', 'class': 'form-control'}))
    particular = forms.CharField(
        widget=forms.TextInput(attrs={'style': 'width: 280px;' 'height: 30px;', 'class': 'form-control'}))
    # alt_qty=forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 100px;' 'height: 30px;', 'class': 'form-control'}))
    qty = forms.DecimalField(
        widget=forms.NumberInput(attrs={'style': 'width: 100px;' 'height: 30px;', 'class': 'form-control'}))
    Uom = forms.CharField(
        widget=forms.TextInput(attrs={'style': 'width: 100px;' 'height: 30px;', 'class': 'form-control'}))
    rate = forms.DecimalField(
        widget=forms.NumberInput(attrs={'style': 'width: 120px;' 'height: 30px;', 'class': 'form-control'}))
    discount = forms.DecimalField(
        widget=forms.NumberInput(attrs={'style': 'width: 120px;' 'height: 30px;', 'class': 'form-control'}))
    amount = forms.DecimalField(
        widget=forms.NumberInput(attrs={'style': 'width: 120px;' 'height: 30px;', 'class': 'form-control'}))


class CalculateForm(forms.Form):
    subtotal = forms.DecimalField(required=False, widget=forms.NumberInput(
        attrs={'style': 'width: 200px;' 'height: 30px;', 'class': 'form-control'}))
    discount = forms.DecimalField(required=False, widget=forms.NumberInput(
        attrs={'style': 'width: 200px;' 'height: 30px;', 'class': 'form-control'}))
    taxable_amount = forms.DecimalField(required=False, widget=forms.NumberInput(
        attrs={'style': 'width: 200px;' 'height: 30px;', 'class': 'form-control'}))
    vat = forms.DecimalField(required=False, widget=forms.NumberInput(
        attrs={'style': 'width: 200px;' 'height: 30px;', 'class': 'form-control'}))
    total_amount = forms.DecimalField(required=False, widget=forms.NumberInput(
        attrs={'style': 'width: 200px;' 'height: 30px;', 'class': 'form-control'}))
    in_words = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'style': 'width: 500px;' 'height: 30px;', 'class': 'form-control'}))
    remarks = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'style': 'width: 500px;' 'height: 80px;', 'class': 'form-control'}))
    received_by = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))
    prepared_by = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))
    authorized_sign = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))
    date_time = forms.DateTimeField(initial=datetime.datetime.now, widget=forms.DateTimeInput(
        attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))


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
                'class':'rounded border-success',
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