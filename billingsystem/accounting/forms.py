from dataclasses import fields
from email.policy import default
from django import forms
import datetime
from .models import customer_bill, bill_item

PAYMENT_CHOICES = (
    ("1", "Cash"),
    ("2", "Credit"),
    ("3", "Card"),
)

class CustomerForm(forms.ModelForm):
    date_time = forms.DateTimeField(initial=datetime.datetime.now)
    class Meta:
        model = customer_bill
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
            'customer_name': forms.TextInput(attrs={'style': 'width: 220px;' 'height: 30px;', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'style': 'width: 220px;' 'height: 30px;', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs = {'style': 'width: 220px;' 'height: 30px;', 'class': 'form-control'}),
            'pan_no': forms.TextInput(attrs={'style': 'width: 220px;' 'height: 30px;', 'class': 'form-control'}),
            'invoice_no': forms.TextInput(attrs={'style': 'width: 160px;' 'height: 30px;', 'class': 'form-control'}),
            'invoice_date': forms.NumberInput(attrs={'type': 'date', 'style': 'width: 160px;' 'height: 30px;', 'class': 'form-control'}),
            'payment_mode': forms.Select(choices=PAYMENT_CHOICES),
            'subtotal': forms.NumberInput(attrs={'style': 'width: 190px;' 'height: 30px;', 'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'style': 'width: 190px;' 'height: 30px;', 'class': 'form-control'}),
            'taxable_amount': forms.NumberInput(attrs={'style': 'width: 190px;' 'height: 30px;', 'class': 'form-control'}),
            'vat': forms.NumberInput(attrs={'style': 'width: 190px;' 'height: 30px;', 'class': 'form-control'}),
            'total_amount': forms.NumberInput(attrs={'style': 'width: 190px;' 'height: 30px;', 'class': 'form-control'}),
            'in_words': forms.TextInput(attrs={'style': 'width: 500px;' 'height: 30px;', 'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'style': 'width: 500px;' 'height: 80px;', 'class': 'form-control'}),
            'received_by': forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}),
            'prepared_by': forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}),
            'authorized_sign': forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}),
        }




# class CustomerForm(forms.Form):
#     customer_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 220px;' 'height: 30px;', 'class': 'form-control'}))
#     address = forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 220px;' 'height: 30px;', 'class': 'form-control'}))
#     phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 220px;' 'height: 30px;', 'class': 'form-control'}))
#     pan_no = forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 220px;' 'height: 30px;', 'class': 'form-control'}))
#     invoice_no = forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 160px;' 'height: 30px;', 'class': 'form-control'}))
#     invoice_date = forms.DateField(initial=datetime.date.today, widget=forms.NumberInput(attrs={'type': 'date', 'style': 'width: 160px;' 'height: 30px;', 'class': 'form-control'}))
#     payment_mode= forms.ChoiceField(choices=PAYMENT_CHOICES)
#     subtotal = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'style': 'width: 200px;' 'height: 30px;', 'class': 'form-control'}))
#     discount = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'style': 'width: 200px;' 'height: 30px;', 'class': 'form-control'}))
#     taxable_amount = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'style': 'width: 200px;' 'height: 30px;', 'class': 'form-control'}))
#     vat = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'style': 'width: 200px;' 'height: 30px;', 'class': 'form-control'}))
#     total_amount = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'style': 'width: 200px;' 'height: 30px;', 'class': 'form-control'}))
#     in_words = forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 500px;' 'height: 30px;', 'class': 'form-control'}))
#     remarks = forms.CharField(required=False, widget=forms.Textarea(attrs={'style': 'width: 500px;' 'height: 80px;', 'class': 'form-control'}))
#     received_by= forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))
#     prepared_by= forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))
#     authorized_sign= forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))
#     date_time = forms.DateTimeField(initial=datetime.datetime.now, widget=forms.DateTimeInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))
  
class ItemForm(forms.ModelForm):
    class Meta:
        model = bill_item

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
            'item_no': forms.TextInput(attrs={'class': 'formset-field','style': 'width: 50px;' 'height: 30px;', 'class': 'form-control'}),
            'particular': forms.Textarea(attrs={'class': 'formset-field', 'style': 'width: 280px;' 'height: 30px;', 'class': 'form-control'}),
            'alt_qty': forms.TextInput(attrs={'class': 'formset-field', 'style': 'width: 80px;' 'height: 30px;', 'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'formset-field', 'style': 'width: 80px;' 'height: 30px;', 'class': 'form-control'}),
            'Uom': forms.TextInput(attrs={'class': 'formset-field', 'style': 'width: 70px;' 'height: 30px;', 'class': 'form-control'}),
            'rate': forms.NumberInput(attrs={'class': 'formset-field', 'style': 'width: 110px;' 'height: 30px;', 'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'formset-field', 'style': 'width: 110px;' 'height: 30px;', 'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'formset-field', 'style': 'width: 110px;' 'height: 30px;', 'class': 'form-control'}),
        }


# class ItemForm(forms.Form):
#     item_no = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 50px;' 'height: 30px;', 'class': 'form-control'}))
#     particular = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 280px;' 'height: 30px;', 'class': 'form-control'}))
#     # alt_qty=forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 100px;' 'height: 30px;', 'class': 'form-control'}))
#     qty = forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 100px;' 'height: 30px;', 'class': 'form-control'}))
#     Uom = forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 100px;' 'height: 30px;', 'class': 'form-control'}))
#     rate = forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 120px;' 'height: 30px;', 'class': 'form-control'}))
#     discount = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'style': 'width: 120px;' 'height: 30px;', 'class': 'form-control'}))
#     amount = forms.DecimalField( widget=forms.NumberInput(attrs={'style': 'width: 120px;' 'height: 30px;', 'class': 'form-control'}))






