from django import forms

PAYMENT_CHOICES =(
    ("1", "Cash"),
    ("2", "Credit"),
    ("3", "Card"),
)

class CustomerForm(forms.Form):
    customer_name = forms.CharField(label='Customer Name', max_length=100)
    address = forms.CharField(label='Address', required=False, max_length=100)
    phone = forms.CharField(label='Phone No', required=False, max_length=15)
    pan_no = forms.CharField(label='PAN', max_length=15)
    invoice_no = forms.CharField(label='Invoice No', max_length=15)
    invoice_date = forms.DateField(label='Invoice Date')
    payment_mode= forms.ChoiceField(choices=PAYMENT_CHOICES)
    received_by= forms.CharField(label='Received By', max_length=100)
    prepared_by= forms.CharField(label='Prepared By', max_length=100)
    authorized_Sign= forms.CharField(label='Authorized Sign', max_length=100)
    date_time = forms.DateTimeField(label='Date & Time')

class ItemForm(forms.Form):
    item_no = forms.CharField(label='S.N')
    particular = forms.TextInput(label='Particular')
    alt_qty=forms.DecimalField(label='Alt Qty')
    qty = forms.DecimalField(label='Qty')
    Uom = forms.CharField(label='Uom')
    rate = forms.DecimalField(label='Rate')
    discount = forms.DecimalField(label='Discount')
    amount = forms.DecimalField(label='Amount')

class CalculateForm(forms.Form):
    subtotal = forms.DecimalField(label='Sub Total')
    discount = forms.DecimalField(label='Discount')
    taxable_amount = forms.DecimalField(label='Taxable Amount')
    vat = forms.DecimalField(label='VAT 13%')
    total_amount = forms.DecimalField(label='Total Amount')
    in_words = forms.Textarea(label='In Words')
    remarks = forms.Textarea(label='Remarks')




