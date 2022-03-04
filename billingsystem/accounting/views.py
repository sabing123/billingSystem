from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.forms import inlineformset_factory
from .forms import CustomerForm, ItemForm, CalculateForm
from django.forms import formset_factory
from django import forms

from .models import *
from .forms import *

from django.contrib import messages


# Create your views here.
def home(request):
    context = {}
    return render(request, 'accounting/index.html', context)


def customer_ledger_detail_page(request, pk):
    customer_ledger = Ledger.objects.get(id=pk)
    customer_ledger_details = customer_ledger.ledger_description_set.all()

    context = {'customer_ledger': customer_ledger, 'customer_ledger_details': customer_ledger_details}
    return render(request, 'accounting/ledgerdetailpage.html', context)


def save_customer_ledger_details(request):
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


def create_ledger(request, pk):
    ledger_descriptionFormSet = inlineformset_factory(Ledger, ledger_description,ledger_descriptionForm, extra=10,
                                          can_delete=False)
    ledger = Ledger.objects.get(id=pk)
    formset = ledger_descriptionFormSet(queryset=ledger_description.objects.none(), instance=ledger)

    if request.method == 'POST':
        formset = ledger_descriptionFormSet(request.POST, instance=ledger)
        if formset.is_valid():
            formset.save()
            return redirect('/ledger')

    context = {'formset': formset, 'ledger': ledger}
    return render(request, 'accounting/createledger.html', context)



def update_ledger_detail(request, pk):
    ledger = ledger_description.objects.get(id=pk)

    formset = ledger_descriptionForm(instance=ledger,)

    if request.method == 'POST':
        formset = ledger_descriptionForm(request.POST, instance=ledger)
        if formset.is_valid():

            formset.save()
            return redirect('/update_ledger/' + str(ledger.pk))
    context = {'formset': formset, 'ledger':ledger}

    return render(request, 'accounting/updateledger.html', context)


def delete_ledger_detail(request, pk):
    ledgerDescription = ledger_description.objects.get(id=pk)

    if request.method == "POST":
        ledgerDescription.delete()
        return redirect('/ledger')

    context = {'item': ledgerDescription}
    return render(request, 'accounting/delete.html', context)

def invoice(request):
    extra_forms = 1
    ItemFormSet = formset_factory(ItemForm, extra=extra_forms)
    if request.method == 'POST':
        customerform = CustomerForm(request.POST)
        calform = CalculateForm(request.POST)
        if 'itemadd' in request.POST and request.POST['itemadd'] == 'true':
            formset_dictionary_copy = request.POST.copy()
            formset_dictionary_copy['form-TOTAL_FORMS'] = int(
                formset_dictionary_copy['form-TOTAL_FORMS']) + extra_forms
            itemform = ItemFormSet(formset_dictionary_copy)
        else:
            itemform = ItemFormSet(request.POST)
            if itemform.is_valid() & customerform.is_valid() & calform.is_valid():
                return HttpResponse('/thankyou')
    else:
        customerform = CustomerForm()
        itemform = ItemFormSet()
        calform = CalculateForm()
    return render(request, 'accounting/invoice.html', {'form': customerform, 'iform': itemform, 'calform': calform})
