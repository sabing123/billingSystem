from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('ledgerdetailpage/<str:pk>/', views.customer_ledger_detail_page, name="ledgerdetailpage"),
    path('ledger/', views.save_customer_ledger_details, name="ledger"),
    path('create_ledger/<str:pk>/', views.create_ledger, name="create_ledger"),
    path('delete_ledger/<str:pk>/', views.delete_ledger_detail, name="delete_ledger"),
    path('update_ledger/<str:pk>/', views.update_ledger_detail, name="update_ledger"),
    path('invoice', views.invoice, name="invoice"),
    path('invoicedetail', views.invoice_detail, name="invoicedetail"),
    path('billupdate/<str:pk>/', views.update_invoice, name="billupdate"),
    path('billdelete/<str:pk>/', views.delete_invoice, name="billdelete"),
]
