# Generated by Django 4.2.6 on 2023-10-31 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentprofile',
            fields=[
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('registration', models.CharField(max_length=20)),
                ('stage1', models.CharField(max_length=20)),
                ('stage2', models.CharField(max_length=20)),
                ('stage3', models.CharField(max_length=20)),
                ('stage4', models.CharField(max_length=20)),
                ('stage5', models.CharField(max_length=20)),
            ],
        ),
    ]
