# Generated by Django 4.1.3 on 2023-01-10 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_accountsuserloginotpmodel_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsuserloginotpmodel',
            name='active',
            field=models.BooleanField(null=True),
        ),
    ]
