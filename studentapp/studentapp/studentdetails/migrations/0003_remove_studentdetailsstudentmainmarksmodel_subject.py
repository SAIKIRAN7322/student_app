# Generated by Django 4.1.3 on 2023-01-03 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentdetails', '0002_studentdetailsstudentmainmarksmodel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdetailsstudentmainmarksmodel',
            name='subject',
        ),
    ]
