from django.db import models
import random
import os
from ecommerce.utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save
from django.urls import reverse


def get_filename_ext(filepath):
	base_name =os.path.basename(filepath)
	name,ext  =os.path.splitext(base_name)
	return ext

def upload_image_path(instance,filename):
	# print(instance)
	# print(filename)
	ext=get_filename_ext(filename)
	new_filename=random.randint(1,1000)
	final_filename='{}{}'.format(new_filename,ext)
	# print(final_filename)
	return 'products/{}'.format(final_filename)


class ProductManager(models.Manager):
	def featured(self):
		return self.get_queryset().filter(featured=True)


	def get_by_id(self,id):
		qs=self.get_queryset().filter(id=id)
		if qs.count()==1:
			return qs.first()
		return None

# Create your models here.
class Product(models.Model):
	title         =models.CharField(max_length=120)
	slug    	  =models.SlugField(blank=True,unique=True)
	description   =models.TextField()
	price		  =models.DecimalField(decimal_places=2,max_digits=10)
	image		  =models.ImageField(upload_to=upload_image_path,null=True,blank=True)
	featured	  =models.BooleanField(default=False)

	objects       =ProductManager()  #custom manager

	def get_absolute_url(self):
		# return "/products/{slug}/".format(slug=self.slug)
		return reverse('product:detail',kwargs={'slug':self.slug})
		
	def __str__(self):
		return self.title

def product_pre_save_receiver(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug=unique_slug_generator(instance)
		# unique_slug_generator(instance)
pre_save.connect(product_pre_save_receiver,sender=Product,weak=False)
