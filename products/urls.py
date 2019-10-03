from django.urls import path
from .import views

urlpatterns = [

    path('display/',views.display,name='display'),
    path('create/',views.create,name='create'),
    path('<int:product_id>',views.detail,name='detail'),
    path('<int:product_id>/deduct',views.deduct,name='deduct'),
    path('receipt/',views.receipt,name='receipt'),
    

]