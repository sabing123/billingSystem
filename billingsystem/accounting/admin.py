from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Ledger)
admin.site.register(ledger_description)
admin.site.register(customer_bill)
admin.site.register(bill_item)
