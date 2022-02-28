from django import forms
import datetime

PAYMENT_CHOICES =(
    ("1", "Cash"),
    ("2", "Credit"),
    ("3", "Card"),
)

class CustomerForm(forms.Form):
    customer_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 220px;' 'height: 30px;', 'class': 'form-control'}))
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 220px;' 'height: 30px;', 'class': 'form-control'}))
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 220px;' 'height: 30px;', 'class': 'form-control'}))
    pan_no = forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 220px;' 'height: 30px;', 'class': 'form-control'}))
    invoice_no = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 160px;' 'height: 30px;', 'class': 'form-control'}))
    invoice_date = forms.DateField(initial=datetime.date.today, widget=forms.NumberInput(attrs={'type': 'date', 'style': 'width: 160px;' 'height: 30px;', 'class': 'form-control'}))
    payment_mode= forms.ChoiceField(choices=PAYMENT_CHOICES)
  
class ItemForm(forms.Form):
    item_no = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 50px;' 'height: 30px;', 'class': 'form-control'}))
    particular = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 280px;' 'height: 30px;', 'class': 'form-control'}))
    # alt_qty=forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 100px;' 'height: 30px;', 'class': 'form-control'}))
    qty = forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 100px;' 'height: 30px;', 'class': 'form-control'}))
    Uom = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100px;' 'height: 30px;', 'class': 'form-control'}))
    rate = forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 120px;' 'height: 30px;', 'class': 'form-control'}))
    discount = forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 120px;' 'height: 30px;', 'class': 'form-control'}))
    amount = forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 120px;' 'height: 30px;', 'class': 'form-control'}))

class CalculateForm(forms.Form):
    subtotal = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'style': 'width: 200px;' 'height: 30px;', 'class': 'form-control'}))
    discount = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'style': 'width: 200px;' 'height: 30px;', 'class': 'form-control'}))
    taxable_amount = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'style': 'width: 200px;' 'height: 30px;', 'class': 'form-control'}))
    vat = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'style': 'width: 200px;' 'height: 30px;', 'class': 'form-control'}))
    total_amount = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'style': 'width: 200px;' 'height: 30px;', 'class': 'form-control'}))
    in_words = forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 500px;' 'height: 30px;', 'class': 'form-control'}))
    remarks = forms.CharField(required=False, widget=forms.Textarea(attrs={'style': 'width: 500px;' 'height: 80px;', 'class': 'form-control'}))
    received_by= forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))
    prepared_by= forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))
    authorized_sign= forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))
    date_time = forms.DateTimeField(initial=datetime.datetime.now, widget=forms.DateTimeInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))





