# Generated by Django 4.1.3 on 2023-01-10 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_accountsuserloginotpmodel_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountsusermodel',
            old_name='phoneNumber',
            new_name='phonenumber',
        ),
    ]
