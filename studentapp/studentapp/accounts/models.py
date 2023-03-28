from django.db import models
from django.db.models.signals import post_save, pre_save
from accounts.utils import statusenumtypes

class accountsUserModel(models.Model):
    phonenumber = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    is_Customer = models.BooleanField(default=False)
    is_Admin = models.BooleanField(default=False)

class accountsUserProfileModel(models.Model):
    owner = models.OneToOneField(accountsUserModel,on_delete=models.CASCADE,related_name="accountsUserProfile_owner")
    name = models.CharField(max_length=100)
    dob = models.DateField()
    image = models.ImageField(blank=True,upload_to="accounts/userimages")
from products.models import creating_usercart, productsPModel

post_save.connect(creating_usercart,sender=accountsUserProfileModel)

class accountsUserLoginOTPModel(models.Model):
    owner = models.ForeignKey(accountsUserModel,on_delete=models.CASCADE,related_name='accountsUserLoginOTPModel_owner')
    otp = models.IntegerField()
    active = models.BooleanField(default=False)

class accountsUserCartProductsModel(models.Model):
    owner = models.ForeignKey(accountsUserModel,on_delete=models.CASCADE,related_name='accountsUserCartProductsModel_owner')
    product = models.ForeignKey(productsPModel,on_delete=models.CASCADE,related_name='accountsUserCartProductsModel_product')
    status = models.CharField(max_length=20,choices=statusenumtypes.choices(),default="Pending")

class accountsUserCartModel(models.Model):
    owner = models.OneToOneField(accountsUserModel,on_delete=models.CASCADE,related_name='accountsUserCartModel_owner')
    products = models.ManyToManyField(accountsUserCartProductsModel)
    finalprice = models.IntegerField(default=0)