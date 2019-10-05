from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
from datetime import date


b=[]
a=0
t=''
# Create your views here.
def display(request):
    pro = Product.objects
    p = Product()
    
    
    
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
        if n == 0:
            return redirect('display')
        product.No_of_items -=1
        temp=list()
        temp.append(product.title)
        a=(n-product.No_of_items)*product.price
        temp.append(n-product.No_of_items)
        temp.append(a)
        b.append(temp)
        product.save()
        return redirect('display')

def receipt(request):
    count=0
    upd_list=list()
    
    
    for i in b:
        a=i[0]
        for z in b:
            if a==z[0]:
                count+=1
        i[1]=count
        count=0

    for i in b:
        if i not in upd_list:
            upd_list.append(i)
    Total=0
    for i in upd_list:
        i.append(i[1]*i[2])

    for i in upd_list:
        Total+=i[3]

    discount='10%'
    pay=Total-(Total*(0.1))    
    return render(request,'products/receipt.html',{'list':upd_list,'total':Total,'discount':discount,'pay':pay})

def clear(request):
    global b
    del b[:]
    return redirect('display')


    
        