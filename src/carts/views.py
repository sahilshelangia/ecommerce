from django.shortcuts import render,redirect
from .models import Cart
from products.models import Product
# Create your views here.

def cart_home(request):
	cart_obj,new_obj=Cart.objects.new_or_get(request)
	return render(request,'carts/home.html',{"cart":cart_obj})

def cart_update(request):
	print(request.POST)
	product_id=request.POST.get('product_id')
	obj=Product.objects.get(id=product_id)
	cart_obj,new_obj=Cart.objects.new_or_get(request)
	if obj in cart_obj.products.all():
		cart_obj.products.remove(obj)
	else:
		cart_obj.products.add(obj)
	request.session['cart_item']=cart_obj.products.count()
	return redirect("carts:home")