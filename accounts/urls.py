from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf import settings
from .import decorators

urlpatterns = [
    path('',views.homepageView.as_view(),name='home'),
    path('signup/',views.productView,name='signup'),
    path('adminsignup/',views.adminView,name='adminsignup'),
    path('dashboard/',views.getEmployee,name='dashboard'),
    path('employeeform/',views.employeeView,name='employeeform'),
    path('verifymobilenumber/',views.otpverifyView,name='verifymobilenumber'),
    path('verifymobile/',decorators.phone_confirmation_required,name='verifymobile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()