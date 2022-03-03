from django.db import models


class Ledger(models.Model):
    c_name = models.CharField(max_length=500, null=True)
    c_code = models.CharField(max_length=200, null=True, blank=True)
    c_date_form_start = models.DateField(null=True, blank=True)
    c_date_form_end = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.c_name


class ledger_description(models.Model):
    c_description = models.CharField(max_length=200, null=True, blank=True)
    c_current_date = models.DateField(null=True, blank=True, default="-")
    c_debt_amt = models.FloatField(null=True, default='0')
    c_credit_amt = models.FloatField(null=True, default='0')
    ledgerDetail = models.ForeignKey(Ledger, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.c_description
