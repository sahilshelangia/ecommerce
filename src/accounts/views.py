from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm,GuestForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.utils.http import is_safe_url
from .models import GuestEmail
from .signals import user_logged_in

# Create your views here.
def login_page(request):
	form=LoginForm(request.POST or None)
	context={
		'form':form,
	}
	if form.is_valid():
		next_=request.GET.get('next')
		next_post=request.POST.get('next')
		redirect_path=next_ or next_post or None
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request,user)
			user_logged_in.send(user.__class__,instance=user,request=request)
			try:
				del request.session['guest_email_id']
			except:
				pass
				
			if is_safe_url(redirect_path,request.get_host()):
				return redirect(redirect_path)
			else:
				return redirect("/")
			    # A backend authenticated the credentials
		else:
		    # No backend authenticated the credentials
		    print("Error")
	return render(request,'accounts/login.html',context=context)

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
	return render(request,'accounts/register.html',context=context)

def guest_register_view(request):
	form=GuestForm(request.POST or None)
	context={
		'form':form,
	}
	if form.is_valid():
		next_=request.GET.get('next')
		next_post=request.POST.get('next')
		redirect_path=next_ or next_post or None
		email=request.POST.get('email')
		new_guest_email=GuestEmail.objects.create(email=email)
		request.session['guest_email_id']=new_guest_email.id
		if is_safe_url(redirect_path,request.get_host()):
			return redirect(redirect_path)
		else:
			return redirect("/")
	return redirect('register')