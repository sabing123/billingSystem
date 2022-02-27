from http.client import HTTPResponse
from django.shortcuts import render
from .forms import CustomerForm, ItemForm, CalculateForm


# Create your views here.
def home(request):
    context = {}
    return render(request, 'accounting/index.html', context)

def invoice(request):
    if request.method == 'POST':
        customerform = CustomerForm(request.POST)
        if customerform.is_valid():
            return HTTPResponse
    else:
        customerform = CustomerForm()
    return render(request, 'accounting/invoice.html', {'form': customerform})
