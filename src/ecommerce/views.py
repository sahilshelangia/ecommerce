from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import ContactForm,LoginForm,RegisterForm
from django.contrib.auth import authenticate,login
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

def login_page(request):
	form=LoginForm(request.POST or None)
	context={
		'form':form,
	}
	if form.is_valid():
		print(form.cleaned_data)
		username=form.cleaned_data.get("username")
		password=form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request,user)
			return redirect("/admin")
		    # A backend authenticated the credentials
		else:
		    # No backend authenticated the credentials
		    print("Error")
	return render(request,'auth/login.html',context=context)

def register_page(request):
	form=RegisterForm(request.POST or None)
	context={
		'form':form,
	}
	if form.is_valid():
		print(form.cleaned_data)
		username=form.cleaned_data.get('username')
		email=form.cleaned_data.get('email')
		password=form.cleaned_data.get('password')
		user = User.objects.create_user(username,email,password)
		user.save()
	return render(request,'auth/register.html',context=context)