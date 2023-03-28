# Generated by Django 4.1.3 on 2023-01-08 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_accountsuserloginotpmodel_owner_and_more'),
        ('products', '0005_alter_productspimagemodel_product_and_more'),
        ('order', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermainmodel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OrderMainModel_owners', to='accounts.accountsusermodel'),
        ),
        migrations.AlterField(
            model_name='ordermainmodel',
            name='products',
            field=models.ManyToManyField(related_name='OrderMainModel_products', to='products.productsusercartpmodel'),
        ),
    ]
