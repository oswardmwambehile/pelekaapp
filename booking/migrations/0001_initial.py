# Generated by Django 5.2.4 on 2025-07-07 09:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
        ('parcel', '0001_initial'),
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=50)),
                ('parcel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcel.parcel')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.route')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.vehicle')),
            ],
        ),
    ]
