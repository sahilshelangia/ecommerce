from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib.auth.models import User
def home_page(request):
	context={
		'title':"sahil yadav",
	}
	if request.user.is_authenticated:
		context['premium_content']="this is only for logged in users."
	return render(request,'home_page.html',context=context);

def about_page(request):
	return render(request,'home_page.html',{});


def contact_page(request):
	contact_form=ContactForm(request.POST or None)
	context={
		'form':contact_form,
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	# if request.method=='POST':
	# 	print(request.POST)
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))
	return render(request,'contact/view.html',context=context);



def bootstrap(request):
	return render(request,'bootstrap/example.html')