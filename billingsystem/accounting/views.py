from email import message
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CustomerForm, ItemForm
from django.forms import modelformset_factory
from .models import *
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from .forms import *
from django.db import transaction, IntegrityError
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
    ledger_descriptionFormSet = inlineformset_factory(Ledger, ledger_description, ledger_descriptionForm, extra=10,
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

    formset = ledger_descriptionForm(instance=ledger, )

    if request.method == 'POST':
        formset = ledger_descriptionForm(request.POST, instance=ledger)
        if formset.is_valid():
            formset.save()
            return redirect('/update_ledger/' + str(ledger.pk))
    context = {'formset': formset, 'ledger': ledger}

    return render(request, 'accounting/updateledger.html', context)


def delete_ledger_detail(request, pk):
    ledgerDescription = ledger_description.objects.get(id=pk)

    if request.method == "POST":
        ledgerDescription.delete()
        return redirect('/ledger')

    context = {'item': ledgerDescription}
    return render(request, 'accounting/delete.html', context)


def invoice(request):
    context = {}
    ItemFormSet = modelformset_factory(Bill, form=ItemForm, extra=5)
    customerform = CustomerForm(request.POST or None)
    itemform = ItemFormSet(request.POST or None, queryset=Bill.objects.none())
    if request.method == 'POST':
        if itemform.is_valid() and customerform.is_valid():
            try:
                with transaction.atomic():
                    customer = customerform.save(commit=False)
                    customer.save()
                    for item in itemform:
                        data = item.save(commit=False)
                        data.invoice_no = customer
                        data.save()
                        messages.success(request, 'Bill saved successfully')
            except IntegrityError:
                print("Error Encountered")
            return redirect("/invoice")
        else:
            messages.error(request, 'Data entered is not correct or invoice number is not unique')
    else:
        context = {'iform':itemform, 'form':customerform}
    return render(request, 'accounting/bill.html', context)

def invoice_detail(request):
    data = Customer.objects.filter().order_by('-id')
    return render(request, 'accounting/invoicedetail.html',{'customerdetail':data})

def update_invoice(request, pk):
    data = Customer.objects.get(id=pk)
    bill = data.invoice.all()
    return render(request, 'accounting/billupdate.html', {'form':data, 'iform':bill})

def delete_invoice(request, pk):
    data = Customer.objects.get(id=pk)
    data.delete()
    messages.success(request, "Customer invoice deleted successfully" )
    return redirect("/invoicedetail")