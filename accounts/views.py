from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
import urllib.request, json 
from django.contrib import messages

# Create your views here.
from accounts.forms import ProductKeyForm, AdminProfileInfoForm, EmpProfileInfoForm,OtpVerifyForm
from accounts.models import ProductKey, AdminProfileInfo, EmployeeProfileInfo
from accounts.decorators import phone_confirmation_required


api_key = "1c9f9aec-a215-11ea-9fa5-0200cd936042"

class homepageView(TemplateView):
    template_name = 'home.html'

def productView(request):
    initial = {'product_key':request.session.get('product_key', None)}
    form = ProductKeyForm(request.POST or None,initial = initial)
    if request.method == 'POST':
        if form.is_valid():
            request.session['product_key'] = form.cleaned_data['product_key']
            return HttpResponseRedirect(reverse('adminsignup'))

    return render(request, 'signup.html',{'form': form})

def adminView(request):
    form = AdminProfileInfoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            prod_value = None
            try:
                prod_value = ProductKey.objects.get(product_key = request.session['product_key'])
            except:
                if prod_value:
                    return redirect(reverse('login'))
                else:
                    user = form.save(commit = False)
                    user.product_key = ProductKey.objects.create(product_key = request.session['product_key'])
                    user.username = form.cleaned_data['username']
                    user.name = form.cleaned_data['name']
                    request.session['mobile_number'] = form.cleaned_data['mobile_number']
                    user.mobile_number = request.session['mobile_number']
                    user.organisation = form.cleaned_data['organisation']
                    user.set_password(form.cleaned_data['password'])
                    user.is_completed = False
                    user.save()
                    return redirect(reverse('verifymobilenumber'))

    return render(request, 'admin_form.html',{'form': form})    

def otpverifyView(request):
    form = OtpVerifyForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            otp_entered = form.cleaned_data['otp_field']
            json_content = {}
            try:
                json_content = urllib.request.urlopen("https://2factor.in/API/V1/"+api_key+"/SMS/VERIFY/"+str(request.session['session_id'])+"/"+str(otp_entered)).read()
                json_content = json.loads(json_content.decode('utf-8'))
            except:
                json_content = {'Details':'Not Matched'}
            if json_content['Details'] == 'OTP Matched':
                user = AdminProfileInfo.objects.filter(product_key__product_key = request.session['product_key']).first()
                user.is_completed = True
                user.save()
                return redirect(reverse('login'))
            else:
                messages.warning(request, 'Entered incorrect OTP, check your mobile for OTP we are sending again')
                form = OtpVerifyForm()

    json_content = urllib.request.urlopen("https://2factor.in/API/V1/"+api_key+"/SMS/"+str(request.session['mobile_number'])+"/AUTOGEN").read()
    json_content = json.loads(json_content.decode('utf-8'))
    request.session['session_id'] = json_content["Details"]

    return render(request,'otpverify.html',{'form':form})
                    


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
@phone_confirmation_required
def getEmployee(request):
    emplist = None
    if request.user.is_authenticated:
        emplist = EmployeeProfileInfo.objects.filter(product_key = request.user.product_key)
    return render(request,'dashboard.html',{"emplist":emplist})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
@phone_confirmation_required
def employeeView(request):
    form = EmpProfileInfoForm(request.POST, request.FILES or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                emp = form.save(commit = False)
                emp.product_key = ProductKey.objects.get(product_key = request.user.product_key)
                emp.employee_name = form.cleaned_data['employee_name']
                emp.employee_id = form.cleaned_data['employee_id']
                emp.employee_mobile_number = form.cleaned_data['employee_mobile_number']
                emp.department = form.cleaned_data['department']
                emp.avatar = form.cleaned_data['avatar']
                emp.save()
                return redirect(reverse('dashboard'))

        return render(request, 'employee_form.html',{'form': form})    
