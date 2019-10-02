from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import grocery,homeutilities,Fooditems,beverages

# Create your views here.
def display(request):
    groceries = grocery.objects
    food = Fooditems.objects
    beverage = beverages.objects
    home = homeutilities.objects


    return render(request,'display.html',{'gro':groceries,'food':food,'bev':beverage,'home':home})

@login_required
def cashier(request):
    groceries = grocery.objects
    food = Fooditems.objects
    beverage = beverages.objects
    home = homeutilities.objects
    if request.method == 'POST':
        
        if request.POST['deduct']:
            
            g = grocery()
            groceries.No_of_items = groceries.No_of_items - request.POST['deduct']
            g.save()
            return redirect('display')
        else:
            return render(request,'display.html',{'gro':groceries,'food':food,'bev':beverage,'home':home},{'error':'login required'})

    else:
        return render(request,'cashier.html',{'gro':groceries,'food':food,'bev':beverage,'home':home})