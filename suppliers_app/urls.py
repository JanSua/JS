from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('suppliers/', views.suppliers),
    path('invoices/', views.invoices),
    path('create_invoice/', views.create_invoice),

]