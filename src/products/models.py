from django.db import models
import random
import os

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
	def get_by_id(self,id):
		qs=self.get_queryset().filter(id=id)
		if qs.count()==1:
			return qs.first()
		return None

# Create your models here.
class Product(models.Model):
	title         =models.CharField(max_length=120)
	description   =models.TextField()
	price		  =models.DecimalField(decimal_places=2,max_digits=10)
	image		  =models.ImageField(upload_to=upload_image_path,null=True,blank=True)
	featured	  =models.BooleanField(default=False)

	objects       =ProductManager()  #custom manager

	def __str__(self):
		return self.title
