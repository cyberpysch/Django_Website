# Generated by Django 4.2.6 on 2023-11-01 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentprofile', '0002_rename_studentprofile_profilesection'),
    ]

    operations = [
        migrations.DeleteModel(
            name='profilesection',
        ),
    ]
