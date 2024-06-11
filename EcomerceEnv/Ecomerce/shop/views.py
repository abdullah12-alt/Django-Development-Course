from django.shortcuts import render,get_object_or_404
from .models import Product,Cart,CartItem,Category
# Create your views here.

def index(request):
    product=Product.objects.all()
    return render(request,"index.html",{"product":product})



def product_detail(request,id):
    product=Product.objects.get(id=id)
    return render(request,"product_detail.html",{"product":product})


def add_to_cart(request,id):
    product=Product.objects.get(id=id)
    cart,created=Cart.objects.get_or_create(user=request.user)
    cart_item,created=CartItem.objects.get_or_create(cart=cart,product=product)
    if not created:
        cart_item.quantity+=1
        cart_item.save()
        return render(request,"cart.html",{"cart":cart})    
    return render(request,"cart.html",{"cart":cart})



    

