# Generated by Django 4.2.4 on 2023-09-14 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_cars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year_produced', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=150)),
            ],
        ),
    ]
