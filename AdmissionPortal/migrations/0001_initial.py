# Generated by Django 4.2.2 on 2023-10-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionEnquiry',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
