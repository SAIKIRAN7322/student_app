# Generated by Django 4.1.3 on 2023-01-07 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productsusercartmodel_productsusercartpmodel_and_more'),
        ('order', '0002_delete_ordermainmodel'),
        ('accounts', '0003_accountsusermodel_accountsuserprofilemodel_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='accountsUser',
        ),
        migrations.DeleteModel(
            name='accountsUserLoginOTPModel',
        ),
        migrations.DeleteModel(
            name='accountsUserProfile',
        ),
        migrations.AddField(
            model_name='accountsuserprofilemodel',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accountsUserProfile_Owner', to='accounts.accountsusermodel'),
        ),
    ]
