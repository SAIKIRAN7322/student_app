import string
from django.db import models
from accounts.models import accountsUserModel
from .utils import statusenumtypes
import random
from django.db.models.signals import pre_save, post_save


def unique_code_generator(sender,instance,*args,**kwargs):
    chars=string.digits
    m = "".join(random.choice(chars) for _ in range(5))
    instance.uniqueCode = "#"+m
def creating_usercart(sender, created, instance, *args, **kwargs):
    from accounts.models import accountsUserCartModel
    print("HIIII", instance.owner, created)
    usercartmodelobject = accountsUserCartModel.objects.create(owner=instance.owner, finalprice=0)

class productsPModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    uniqueCode = models.CharField(max_length=100,unique=True,blank = True)
    price = models.IntegerField(default=0)

pre_save.connect(unique_code_generator,sender=productsPModel)




class productsPImageModel(models.Model):
    product = models.ForeignKey(productsPModel,on_delete=models.CASCADE,related_name="productsPImage_product")
    image = models.ImageField(blank=True)




