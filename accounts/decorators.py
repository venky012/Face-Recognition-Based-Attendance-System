from django.contrib import messages
import urllib.request, json 
from django.shortcuts import render, redirect
from django.urls import reverse


from .models import AdminProfileInfo
from .forms import OtpVerifyForm



api_key = "1c9f9aec-a215-11ea-9fa5-0200cd936042"


def phone_confirmation_required(function):

    def checker(request, *args, **kwargs):
        if request.user.is_staff is True:
            return function(request, *args, **kwargs)
        elif request.user.is_completed is True:
            return function(request, *args, **kwargs)
        else:
            form = OtpVerifyForm(request.POST or None)
            print("1-----------------------------------------------------------------------------")
            if request.method == 'POST':
                print(form,'request-------------------------------')
                if form.is_valid():
                    print(form,'validated----------------------------')
                    otp_entered = form.cleaned_data['otp_field']
                    print(otp_entered)
                    print(request.session['session_id'])
                    json_content = {}
                    try:
                        json_content = urllib.request.urlopen("https://2factor.in/API/V1/"+api_key+"/SMS/VERIFY/"+str(request.session['session_id'])+"/"+str(otp_entered)).read()
                        json_content = json.loads(json_content.decode('utf-8'))
                    except:
                        json_content = {'Details':'Not Matched'}
                    print(json_content)
                    if json_content['Details'] == 'OTP Matched':
                        user = AdminProfileInfo.objects.filter(product_key__product_key = request.user.product_key).first()
                        print(user.username,user.organisation,user.mobile_number)
                        user.is_completed = True
                        user.save()
                        print("done--------------------------------------")
                        return redirect(reverse('dashboard'))
                    else:
                        messages.warning(request, 'Entered incorrect OTP, check your mobile for OTP we are sending again')
                        form = OtpVerifyForm()

            json_content = urllib.request.urlopen("https://2factor.in/API/V1/"+api_key+"/SMS/"+str(request.user.mobile_number)+"/AUTOGEN").read()
            json_content = json.loads(json_content.decode('utf-8'))
            request.session['session_id'] = json_content["Details"]

            return render(request,'otpverify.html',{'form':form}) 
    return checker