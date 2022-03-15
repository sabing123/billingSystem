from django.db import models


class Ledger(models.Model):
    c_name = models.CharField(max_length=500, null=True)
    c_code = models.CharField(max_length=200, null=True, blank=True)
    c_date_form_start = models.DateField(null=True, blank=True)
    c_date_form_end = models.DateField(null=True, blank=True)

    def __str__(self):
        if self.c_name == None:
            return "Empty!! Name is not inserted"
        return self.c_name


class ledger_description(models.Model):
    c_description = models.CharField(max_length=200, null=True, blank=True)
    c_current_date = models.DateField(null=True, blank=True, default="-")
    c_debt_amt = models.FloatField(null=True, default='0')
    c_credit_amt = models.FloatField(null=True, default='0')
    ledgerDetail = models.ForeignKey(Ledger, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        if self.c_description == None:
            return "Empty!! Description is not inserted"
        return self.c_description


class Customer(models.Model):
    PAYMENT_CHOICES = (
        ("1", "Cash"),
        ("2", "Credit"),
        ("3", "Card"),
    )
    customer_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    pan_no = models.CharField(max_length=200)
    invoice_no = models.CharField(max_length=200, unique=True)
    invoice_date = models.DateField()
    payment_mode = models.CharField(choices=PAYMENT_CHOICES, max_length=50)
    subtotal = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    discount = models.DecimalField(max_digits=20, decimal_places=2)
    taxable_amount = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    vat = models.DecimalField(max_digits=20, decimal_places=2)
    total_amount = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    in_words = models.CharField(max_length=500, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    received_by = models.CharField(max_length=200, blank=True, null=True)
    prepared_by = models.CharField(max_length=200)
    authorized_sign = models.CharField(max_length=200, blank=True, null=True)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name


class Bill(models.Model):
    item_no = models.CharField(max_length=10, blank=True, null=True)
    particular = models.CharField(max_length=200, blank=True, null=True)
    alt_qty = models.IntegerField(default=0, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    Uom = models.CharField(max_length=100, blank=True, null=True)
    rate = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    discount = models.DecimalField(default=0, decimal_places=2, max_digits=20, blank=True, null=True)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=20, blank=True, null=True)
    invoice_no = models.ForeignKey(Customer, related_name='invoice', on_delete=models.CASCADE)

    def __str__(self):
        return self.item_no
