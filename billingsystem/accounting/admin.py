from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Ledger)
admin.site.register(ledger_description)
admin.site.register(Customer)
admin.site.register(Bill)
