# Generated by Django 4.1.3 on 2023-01-07 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0004_productspimagemodel'),
        ('accounts', '0005_accountsuserloginotpmodel'),
        ('order', '0002_delete_ordermainmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderMainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finalPrice', models.IntegerField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.accountsusermodel')),
                ('products', models.ManyToManyField(to='products.productsusercartpmodel')),
            ],
        ),
    ]
