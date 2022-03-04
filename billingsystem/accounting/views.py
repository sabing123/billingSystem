
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomerForm, ItemForm
from django.forms import formset_factory

from .forms import CustomerForm, ItemForm
from django.forms import formset_factory, modelformset_factory
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


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
        return render(request, 'accounting/invoice.html', context)


        customerform = CustomerForm()
        itemform = ItemFormSet()
        calform = CalculateForm()
    return render(request, 'accounting/invoice.html', {'form': customerform, 'iform': itemform, 'calform': calform})

def c_ledger(request):
    ledger_d = ledgerDetail.objects.all()
    context = {'ledger_d': ledger_d}
    return render(request, 'accounting/ledger.html', context)


def ledger_detail_page(request, pk):
    customer_ledger = ledgerDetail.objects.get(id=pk)
    customer_ledger_details = customer_ledger.ledger_description_set.all()
    context = {'customer_ledger': customer_ledger, 'customer_ledger_details': customer_ledger_details}

    return render(request, 'accounting/ledgerdetailpage.html', context)


 # if 'itemadd' in request.POST and request.POST['itemadd'] == 'true':
        #     formset_dictionary_copy = request.POST.copy()
        #     formset_dictionary_copy['form-TOTAL_FORMS'] = int(
        #         formset_dictionary_copy['form-TOTAL_FORMS']) + extra_forms
        #     itemform = ItemFormSet(formset_dictionary_copy)
        # else:



         # customer = customer_bill()
                # item = bill_item()
                # customer.customer_name = customerform.cleaned_data['customer_name']
                # customer.address = customerform.cleaned_data['address']
                # customer.phone = customerform.cleaned_data['phone']
                # customer.pan_no = customerform.cleaned_data['pan_no']
                # customer.invoice_no = customerform.cleaned_data['invoice_no']
                # customer.invoice_date = customerform.cleaned_data['invoice_date']
                # customer.payment_mode = customerform.cleaned_data['payment_mode']
                # customer.subtotal = customerform.cleaned_data['subtotal']
                # customer.discount = customerform.cleaned_data['discount']
                # customer.vat = customerform.cleaned_data['vat']
                # customer.total_amount = customerform.cleaned_data['total_amount']
                # customer.received_by = customerform.cleaned_data['received_by']
                # customer.prepared_by = customerform.cleaned_data['prepared_by']
                # customer.authorized_sign = customerform.cleaned_data['authorized_sign']
                # customer.date_time = customerform.cleaned_data['date_time']
                # for itemforms in itemform:
                #     item.item_no = itemforms.save['item_no']
                #     item.particular = itemforms.cleaned_data['particular']
                #     item.quantity = itemforms.cleaned_data['qty']
                #     item.Uom = itemforms.cleaned_data['Uom']
                #     item.rate = itemform.cleaned_data['rate']
                #     item.discount = itemform.cleaned_data['discount']
                #     item.amount = itemform.cleaned_data['amount']
                #     item.invoice_no = customerform.cleaned_data['invoice_no']
                #     item.save()