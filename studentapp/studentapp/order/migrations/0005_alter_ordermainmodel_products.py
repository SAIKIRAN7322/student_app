# Generated by Django 4.1.3 on 2023-01-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_accountsusercartproductsmodel_accountsusercartmodel'),
        ('order', '0004_alter_ordermainmodel_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermainmodel',
            name='products',
            field=models.ManyToManyField(related_name='OrderMainModel_products', to='accounts.accountsusercartproductsmodel'),
        ),
    ]