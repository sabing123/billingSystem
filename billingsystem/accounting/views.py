from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomerForm, ItemForm
from django.forms import modelformset_factory
from django.shortcuts import render
from .models import *
from django.db import transaction, IntegrityError


# Create your views here.
def home(request):
    context = {}
    return render(request, 'accounting/index.html', context)


def invoice(request):
    context = {}
    ItemFormSet = modelformset_factory(bill_item, form=ItemForm)
    customerform = CustomerForm(request.POST or None)
    itemform = ItemFormSet(request.POST or None, queryset= bill_item.objects.none())
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
                      
            except IntegrityError:
                print("Error Encountered")
                
            return HttpResponse('/about/thankyou') 
    else:
        context = {'iform':itemform, 'form':customerform}
    return render(request, 'accounting/bill.html', context)


def c_ledger(request):
    ledger_d = ledgerDetail.objects.all()
    context = {'ledger_d': ledger_d}
    return render(request, 'accounting/ledger.html', context)


def ledger_detail_page(request, pk):
    customer_ledger = ledgerDetail.objects.get(id=pk)
    customer_ledger_details = customer_ledger.ledger_description_set.all()
    context = {'customer_ledger': customer_ledger, 'customer_ledger_details': customer_ledger_details}

    return render(request, 'accounting/ledgerdetailpage.html', context)

def invoice_detail(request):
    invoice= customer_bill.bill_item_set.all()
    return render(request, 'accounting/invoicedetail.html',{'customerdetail':invoice})

