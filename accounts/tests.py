from django.test import TestCase

# Create your tests here.


# def sign_up_view(request):
#     if request.method == 'GET':
#         prod_form = ProductKeyForm()
#     else:
#         prod_form = ProductKeyForm(request.POST)
#         print(prod_form,"---------------------------------------------------------------------")
#         if prod_form.is_valid():
#             user = prod_form.save(commit=False)
#             prod_value = prod_form.cleaned_data['product_key']
#             user.product_key = prod_value
#             admin_obj = AdminProfileInfo.objects.filter(product_key = prod_form.cleaned_data['product_key'])
#             prod_obj = ProductKey.objects.filter(product_key = prod_form.cleaned_data['product_key'])
#             prod_completed = False
#             admin_completed = False
#             for obj in prod_obj:
#                 if obj.product_key:
#                     prod_completed = True
#             for obj in admin_obj:
#                 if obj.is_completed:
#                     admin_completed = True

#             if admin_completed:
#                 print('--------------------your account was already created. please login--------------------')
#                 return 
#             else:
#                 print("---------------------------account created successfully------------------")
#                 if not prod_completed:
#                     user.save()
#                 # print(request.method)
#                 # admin form from here
#                 if request.method == "GET":
#                     admin_form = AdminProfileInfoForm()
#                     print("insideget---------------------------------")
#                 else:
#                     admin_form = AdminProfileInfoForm(request.POST)
#                     print("---------------------------in admin account creation------------------",admin_form.is_valid)
#                     if admin_form.is_valid():
#                         print("inside form validated---------------------")
#                         admin = admin_form.save(commit = False)
#                         admin.product_key = ProductKey.objects.get(product_key = prod_value)
#                         admin.username = admin_form.cleaned_data['username']
#                         admin.name = admin_form.cleaned_data['name']
#                         admin.mobile_number = admin_form.cleaned_data['mobile_number']
#                         admin.organisation = admin_form.cleaned_data['organisation']
#                         admin.is_completed = True
#                         admin.save()
#                         print('------------------------admin profile created--------------------------')
                    

#                 return render(request,'admin_form.html',{'form':admin_form})
#     return render(request, 'signup.html',{'form': prod_form})