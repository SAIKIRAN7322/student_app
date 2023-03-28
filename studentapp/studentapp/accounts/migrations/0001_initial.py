# Generated by Django 4.1.3 on 2023-01-06 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accountsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhoneNumber', models.IntegerField(unique=True)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Is_Customer', models.BooleanField(default=False)),
                ('Is_Admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='accountsUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('Image', models.ImageField(blank=True, upload_to='')),
                ('Owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.accountsuser')),
            ],
        ),
        migrations.CreateModel(
            name='accountsUserLoginOTPModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OTP', models.IntegerField()),
                ('Active', models.BooleanField()),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.accountsuser')),
            ],
        ),
    ]
