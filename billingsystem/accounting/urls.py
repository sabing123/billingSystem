from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
<<<<<<< HEAD
    path('invoice', views.invoice, name="invoice"),
=======
    path('ledger/', views.c_ledger, name="ledger"),
    path('ledgerdetailpage/<str:pk>/', views.ledger_detail_page, name="ledgerdetailpage"),
>>>>>>> origin/sabin
]
