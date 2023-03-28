# Generated by Django 4.1.3 on 2023-01-08 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_accountsuserloginotpmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsuserloginotpmodel',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='accountsUserLoginOTPModel_owner', to='accounts.accountsusermodel'),
        ),
        migrations.AlterField(
            model_name='accountsuserprofilemodel',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accountsUserProfile_owner', to='accounts.accountsusermodel'),
        ),
    ]
