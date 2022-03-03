from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('ledger/', views.c_ledger, name="ledger"),
    path('ledgerdetailpage/<str:pk>/', views.ledger_detail_page, name="ledgerdetailpage"),
    path('create_ledger/<str:pk>/', views.create_ledger_page, name="create_ledger"),
]
