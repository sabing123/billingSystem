from email.policy import default
from django import forms

PAYMENT_CHOICES =(
    ("1", "Cash"),
    ("2", "Credit"),
    ("3", "Card"),
)

class CustomerForm(forms.Form):
    customer_name = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))
    pan_no = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))
    invoice_no = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 160px;' 'height: 30px;', 'class': 'form-control'}))
    invoice_date = forms.DateField(widget=forms.DateInput(attrs={'style': 'width: 160px;' 'height: 30px;', 'class': 'form-control'}))
    payment_mode= forms.ChoiceField(choices=PAYMENT_CHOICES)
    received_by= forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))
    prepared_by= forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))
    authorized_sign= forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))
    date_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'style': 'width: 180px;' 'height: 30px;', 'class': 'form-control'}))

class ItemForm(forms.Form):
    item_no = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 60px;' 'height: 30px;', 'class': 'form-control'}))
    particular = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 250px;' 'height: 30px;', 'class': 'form-control'}))
    alt_qty=forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 100px;' 'height: 30px;', 'class': 'form-control'}))
    qty = forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 100px;' 'height: 30px;', 'class': 'form-control'}))
    Uom = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100px;' 'height: 30px;', 'class': 'form-control'}))
    rate = forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 100px;' 'height: 30px;', 'class': 'form-control'}))
    discount = forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 100px;' 'height: 30px;', 'class': 'form-control'}))
    amount = forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 100px;' 'height: 30px;', 'class': 'form-control'}))

class CalculateForm(forms.Form):
    subtotal = forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 190px;' 'height: 30px;', 'class': 'form-control'}))
    discount = forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 190px;' 'height: 30px;', 'class': 'form-control'}))
    taxable_amount = forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 190px;' 'height: 30px;', 'class': 'form-control'}))
    vat = forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 190px;' 'height: 30px;', 'class': 'form-control'}))
    total_amount = forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 190px;' 'height: 30px;', 'class': 'form-control'}))
    in_words = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 300px;' 'height: 30px;', 'class': 'form-control'}))
    remarks = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 300px;' 'height: 30px;', 'class': 'form-control'}))




