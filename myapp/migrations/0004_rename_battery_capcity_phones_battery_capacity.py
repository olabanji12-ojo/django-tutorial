# Generated by Django 4.2.4 on 2023-09-10 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_phones'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phones',
            old_name='battery_capcity',
            new_name='battery_capacity',
        ),
    ]
