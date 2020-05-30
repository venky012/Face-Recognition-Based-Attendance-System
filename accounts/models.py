from django.db import models
# Create your models here.
import os
from uuid import uuid4

from django.contrib.auth.models import AbstractUser

class ProductKey(models.Model):
	product_key = models.CharField(max_length=50,blank=False,unique = True)

	def __str__(self):
		return self.product_key

class AdminProfileInfo(AbstractUser):
	product_key = models.OneToOneField(ProductKey,on_delete=models.CASCADE,null=True)
	# username = models.CharField(max_length=10,unique = True,blank = False)
	# password = models.CharField(blank = False)
	name = models.CharField(max_length=50,blank=False)
	mobile_number = models.CharField(max_length=15,blank = False)
	organisation = models.CharField(max_length=50,blank=False)
	is_completed = models.BooleanField(default = False)		# for otp verification


	def __str__(self):
		return self.username

def update_filename(instance, filename):
    upload_to = 'photos'
    ext = filename.split('.')[-1]
    if instance.employee_id:
        filename = '{}.{}'.format(instance.employee_id, ext)
    return os.path.join(upload_to, filename)

class EmployeeProfileInfo(models.Model):
	product_key = models.ForeignKey(ProductKey,on_delete=models.CASCADE)
	employee_name = models.CharField(max_length=50,blank=False)
	employee_id = models.CharField(max_length=15,unique=True,blank=False)
	employee_mobile_number = models.CharField(max_length=15,blank=False)
	department = models.CharField(max_length=50,blank=False)
	avatar = models.ImageField(upload_to=update_filename)

	def __str__(self):
		return self.employee_name