# Generated by Django 4.2 on 2025-07-08 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_route_created_at_route_updated_at_route_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name_plural': 'disticts'},
        ),
    ]
