from django import forms
from django.core.files.images import get_image_dimensions
from accounts.models import EmployeeProfileInfo, AdminProfileInfo,ProductKey

# class SignupForm(forms.Form):
# 	product_key = forms.CharField(max_length=15,required=True)
# 	username = forms.CharField(max_length=10,required = True)
# 	password = forms.CharField(widget = forms.PasswordInput)
# 	password2 = forms.CharField(widget = forms.PasswordInput)
# 	name = forms.CharField(max_length=50,required = True)
# 	mobile_number = forms.CharField(max_length=10,required = True)
# 	organisation = forms.CharField(max_length=50,required = True)
	
# 	def clean_password2(self):
# 		cd = self.cleaned_data
# 		if cd['password'] != cd['password2']:
# 			raise forms.ValidationError('Passwords don\'t match.')
# 		return cd['password2']

class ProductKeyForm(forms.ModelForm):
	product_key = forms.CharField(max_length=15,required=True)
	class Meta:
		model = ProductKey
		fields = ('product_key',)

class AdminProfileInfoForm(forms.ModelForm):
	username = forms.CharField(max_length=10,required = True)
	password = forms.CharField(widget = forms.PasswordInput)
	password2 = forms.CharField(widget = forms.PasswordInput)
	name = forms.CharField(max_length=50,required = True)
	mobile_number = forms.CharField(max_length=15,required = True)
	organisation = forms.CharField(max_length=50,required = True)
	class Meta:
		model = AdminProfileInfo
		fields = ('username','name','mobile_number','organisation','password','password2')


	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match.')
		return cd['password2']


class EmpProfileInfoForm(forms.ModelForm):
	employee_name = forms.CharField(max_length=50,required=True)
	employee_id = forms.CharField(max_length=15,required=True)
	employee_mobile_number = forms.CharField(max_length=15,required=True)
	department = forms.CharField(max_length=50,required=True)
	avatar = forms.ImageField()
	class Meta:
		model = EmployeeProfileInfo
		fields = ('employee_name','employee_id','employee_mobile_number','department','avatar')
	
	def clean_avatar(self):
		avatar = self.cleaned_data['avatar']
		return avatar

class OtpVerifyForm(forms.Form):
	otp_field = forms.CharField(max_length = 10, required = True)