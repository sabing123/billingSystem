from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import *

from django.contrib import messages


# Create your views here.
def home(request):
    context = {}
    return render(request, 'accounting/index.html', context)


def c_ledger(request):
    ledger_d = ledgerDetail.objects.all()
    context = {'ledger_d': ledger_d}
    return render(request, 'accounting/ledger.html', context)


def ledger_detail_page(request, pk):
    customer_ledger = ledgerDetail.objects.get(id=pk)
    customer_ledger_details = customer_ledger.ledger_description_set.all()
    context = {'customer_ledger': customer_ledger, 'customer_ledger_details': customer_ledger_details}

    return render(request, 'accounting/ledgerdetailpage.html', context)

