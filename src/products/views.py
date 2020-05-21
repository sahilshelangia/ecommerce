from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Product
from carts.models import Cart
from analytics.mixins import ObjectViewedMixin

class ProductFeaturedListView(ListView):
	template_name='products/list.html'	
	def get_queryset(self,*args,**kwargs):
		request=self.request
		return Product.objects.featured()

class ProductFeaturedDetailView(ObjectViewedMixin,DetailView):
	template_name='products/featured-detail.html'

	def get_queryset(self,*args,**kwargs):
		request=self.request
		return Product.objects.featured()
	# def get_context_data(self,*args,**kwargs):
	# 	context=super(ProductDetailView,self).get_context_data(*args,**kwargs)
	# 	print(context)
	

class ProductListView(ListView):
	queryset=Product.objects.all()
	template_name='products/lists.html'

	# def get_context_data(self,*args,**kwargs):
	# 	context=super(ProductListView,self).get_context_data(*args,**kwargs)
	# 	return context

def product_list_view(request):
	queryset=Product.objects.all()
	context={
		'object_list':queryset,
	}
	return render(request,'products/list.html',context)

class ProductDetailView(ObjectViewedMixin,DetailView):
	queryset=Product.objects.all()
	template_name='products/detail.html'

	# def get_context_data(self,*args,**kwargs):
	# 	context=super(ProductDetailView,self).get_context_data(*args,**kwargs)
	# 	print(context)
	# 	return context


class ProductDetailSlugView(ObjectViewedMixin,DetailView):
	queryset=Product.objects.all()
	template_name='products/detail.html'
	
	def get_context_data(self,*args,**kwargs):
		context=super(ProductDetailSlugView,self).get_context_data(*args,**kwargs)
		cart_obj,new_obj=Cart.objects.new_or_get(self.request)
		context['cart']=cart_obj
		return context

	def get_object(self,*args,**kwargs):
		request=self.request
		slug=self.kwargs.get('slug')
		try:
			instance=get_object_or_404(Product,slug=slug)
		except Product.DoesNotExist:
			raise Http404("Not found...")
		except Product.MultipleObjectsReturned:
			qs=Product.objects.all().filter(slug=slug)
			instance=qs.first()
		except:
			raise Http404("Uhmmmm")
		# object_viewed_signal.send(instance.__class__,instance=instance,request=request)
		return instance



	# def get_context_data(self,*args,**kwargs):
	# 	context=super(ProductDetailView,self).get_context_data(*args,**kwargs)
	# 	print(context)
	# 	return context


def product_detail_view(request,pk):
	# instance=get_object_or_404(Product,pk=pk)
	instance=Product.objects.get_by_id(pk)
	if instance is None:
		raise Http404("Product doesn't exist!")
	context={
		'object':instance,
	}
	return render(request,'products/detail.html',context)
