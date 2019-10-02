from django.urls import path
from . import views

urlpatterns = [

    path('display/',views.display,name='display'),
    path('cashier/',views.cashier,name='cashier'),
    

]