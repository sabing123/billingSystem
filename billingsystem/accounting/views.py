from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomerForm, ItemForm, CalculateForm
from django.forms import formset_factory

# Create your views here.
def home(request):
    context = {}
    return render(request, 'accounting/index.html', context)

def invoice(request):
    extra_forms = 2
    ItemFormSet = formset_factory(ItemForm, extra=extra_forms,  max_num=20)
    if request.method == 'POST':
        if 'additems' in request.POST and request.POST['additems'] == 'true':
            formset_dictionary_copy = request.POST.copy()
            formset_dictionary_copy['form-TOTAL_FORMS'] = int(formset_dictionary_copy['form-TOTAL_FORMS']) + extra_forms
            formset = ItemFormSet(formset_dictionary_copy)
        else:
            formset = ItemFormSet(request.POST)
            customerform = CustomerForm(request.POST)
            calform = CalculateForm(request.POST)
            if customerform.is_valid() & formset.is_valid() & calform.is_valid():
                return HttpResponse('/about/contact/thankyou')
    else:
        customerform = CustomerForm()
        formset = ItemFormSet()
        calform = CalculateForm()
    return render(request, 'accounting/invoice.html', {'form': customerform, 'iform': formset, 'calform': calform})
