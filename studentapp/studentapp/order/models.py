from django.db import models

from accounts.models import accountsUserModel,accountsUserCartProductsModel

from order.utils import statusenumtypes

class OrderMainModel(models.Model):
    owner = models.ForeignKey(accountsUserModel,on_delete=models.CASCADE,related_name="OrderMainModel_owners")
    products = models.ManyToManyField(accountsUserCartProductsModel,related_name="OrderMainModel_products")
    finalPrice = models.IntegerField()
    status = models.CharField(max_length=100,choices=statusenumtypes.choices())