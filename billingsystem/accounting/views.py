from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomerForm, ItemForm, CalculateForm
from django.forms import formset_factory

# Create your views here.
def home(request):
    context = {}
    return render(request, 'accounting/index.html', context)


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
