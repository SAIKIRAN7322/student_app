from django.contrib import admin

from accounts.models import accountsUserModel, accountsUserProfileModel, accountsUserCartProductsModel, \
    accountsUserCartModel

# Register your models here.
admin.site.register(accountsUserModel)
admin.site.register(accountsUserProfileModel)
admin.site.register(accountsUserCartProductsModel)
admin.site.register(accountsUserCartModel)