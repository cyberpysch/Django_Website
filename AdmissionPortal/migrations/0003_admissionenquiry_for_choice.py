# Generated by Django 4.2.6 on 2023-10-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdmissionPortal', '0002_admissionenquiry_address_admissionenquiry_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissionenquiry',
            name='For_choice',
            field=models.CharField(default='', max_length=15),
        ),
    ]
