from django.contrib import admin
from accounts.models import AdminProfileInfo,EmployeeProfileInfo,ProductKey
# Register your models here.

admin.site.register(ProductKey)
admin.site.register(AdminProfileInfo)
admin.site.register(EmployeeProfileInfo)