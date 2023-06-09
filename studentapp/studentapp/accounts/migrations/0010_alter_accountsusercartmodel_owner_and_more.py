# Generated by Django 4.1.3 on 2023-01-10 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_productsusercartpmodel_owner_and_more'),
        ('accounts', '0009_accountsusercartproductsmodel_accountsusercartmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsusercartmodel',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accountsUserCartModel_owner', to='accounts.accountsusermodel'),
        ),
        migrations.AlterField(
            model_name='accountsusercartproductsmodel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountsUserCartProductsModel_owner', to='accounts.accountsusermodel'),
        ),
        migrations.AlterField(
            model_name='accountsusercartproductsmodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountsUserCartProductsModel_product', to='products.productspmodel'),
        ),
        migrations.AlterField(
            model_name='accountsuserloginotpmodel',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='accountsuserloginotpmodel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountsUserLoginOTPModel_owner', to='accounts.accountsusermodel'),
        ),
    ]
