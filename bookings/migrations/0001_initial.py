# Generated by Django 3.2.17 on 2023-02-14 12:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guests', models.CharField(choices=[('1 guest', '1 guest'), ('2 guests', '2 guests'), ('3 guests', '3 guests'), ('4 guests', '4 guests'), ('5 guests', '5 guests'), ('6 guests', '6 guests'), ('7 guests', '7 guests'), ('8 guests', '8 guests')], default='1 guest', max_length=50)),
                ('First_name', models.CharField(help_text='First name', max_length=20)),
                ('Last_name', models.CharField(help_text='Last name', max_length=20)),
                ('Email', models.EmailField(help_text='Email', max_length=20)),
                ('Phone', models.CharField(help_text='Phone', max_length=20)),
                ('day', models.DateField(default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('9 AM', '9 AM'), ('10 AM', '10 AM'), ('11 AM', '11 AM'), ('12 PM', '12 PM'), ('1 PM', '1 PM'), ('2 PM', '2 PM'), ('3 PM', '3 PM'), ('4 PM', '4 PM'), ('5 PM', '5 PM'), ('6 PM', '6 PM'), ('7 PM', '7 PM'), ('8 PM', '8 PM'), ('9 PM', '9 PM')], max_length=10)),
                ('time_ordered', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
