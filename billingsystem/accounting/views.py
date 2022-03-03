from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.forms import inlineformset_factory
from django import forms

from .models import *
from .forms import *

from django.contrib import messages


# Create your views here.
def home(request):
    context = {}
    return render(request, 'accounting/index.html', context)


def create_ledger_page(request, pk):
    LedgerFormSet = inlineformset_factory(Ledger, ledger_description, ledger_descriptionForm, extra=2,
                                          can_delete=False)
    ledger = Ledger.objects.get(id=pk)
    formset = LedgerFormSet(queryset=ledger_description.objects.none(), instance=ledger)

    if request.method == 'POST':
        formset = LedgerFormSet(request.POST, instance=ledger)
        if formset.is_valid():
            formset.save()
            return redirect('/ledger')

    context = {'formset': formset, 'ledger': ledger}
    return render(request, 'accounting/createledger.html', context)


def c_ledger(request):
    ledger_d = Ledger.objects.all()
    LedgerForms = LedgerForm()

    if request.method == "POST":
        # print("pf : ", request.POST)
        form = LedgerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ledger')

    context = {'ledger_d': ledger_d, 'LedgerForms': LedgerForms, }

    return render(request, 'accounting/ledger.html', context)


def ledger_detail_page(request, pk):
    customer_ledger = Ledger.objects.get(id=pk)
    customer_ledger_details = customer_ledger.ledger_description_set.all()
    context = {'customer_ledger': customer_ledger, 'customer_ledger_details': customer_ledger_details}

    return render(request, 'accounting/ledgerdetailpage.html', context)
