from django import forms
from django.contrib.auth.models import User
class LoginForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput(
		attrs={
			"class":"form-control",
			"placeholder":"username"
		}
	))
	password=forms.CharField(widget=forms.PasswordInput(
		attrs={
			"class":"form-control",
			"placeholder":"password"
		}
	))

class RegisterForm(forms.Form):
	username=forms.CharField()
	email=forms.EmailField()
	password=forms.CharField(widget=forms.PasswordInput)
	password2=forms.CharField(widget=forms.PasswordInput,label='confirm password')


	def clean_username(self):
		username=self.cleaned_data.get('username')
		qs=User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("username is already taken")
		return username

	def clean_email(self):
		email=self.cleaned_data.get('email')
		qs=User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email is already taken")
		return email

	def clean(self):
		data=self.cleaned_data
		password=self.cleaned_data.get('password')
		password2=self.cleaned_data.get('password2')
		if password2!=password:
			raise forms.ValidationError("password didn't match")
		return data

class GuestForm(forms.Form):
	email=forms.EmailField()