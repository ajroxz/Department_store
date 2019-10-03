from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

b=list()
a=0
# Create your views here.
def display(request):
    pro = Product.objects


    return render(request,'products/display.html',{'product':pro})

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['image'] and request.POST['price']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            product.image = request.FILES['image']
            product.price = int(request.POST['price'])
            product.pub_date = timezone.datetime.now()
            product.No_of_items = 100
            product.hunter =request.user
            product.save()

            return redirect('/products/'+ str(product.id))
        else:
            return render(request,'products/create.html',{'error':'All fields are required.'})

    else:
        return render(request,'products/create.html')   

def detail(request, product_id):
    product = get_object_or_404(Product,pk=product_id)
    return render(request,'products/detail.html',{'product':product})

@login_required
def deduct(request,product_id):
    if request.method=='POST':
        product = get_object_or_404(Product,pk=product_id)
        n=product.No_of_items
        product.No_of_items -=1
        temp=list()
        temp.append(product.title)
        global a
        global b
        a=(n-product.No_of_items)*product.price
        temp.append(a)
        b.append(temp)
        product.save()
        return redirect('display')

def receipt(request):
    global a
    global b
    return render(request,'products/receipt.html',{'total':b})