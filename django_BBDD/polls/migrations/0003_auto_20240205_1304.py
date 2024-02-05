# Generated by Django 3.2.12 on 2024-02-05 13:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20240205_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userImg', models.URLField(verbose_name='userImg')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('phone', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(code='invalid_registration', message='Enter a valid format phone number', regex='^(0|91)?[6-9][0-9]{8}')])),
                ('date', models.DateField()),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=255)),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('is_archived', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='job',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Receptionist', 'Receptionist'), ('Cleaning Room', 'Cleaning Room')], max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=9, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_registration', message='Enter a valid format phone number', regex='^(0|91)?[6-9][0-9]{8}')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.URLField(verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=10),
        ),
    ]
