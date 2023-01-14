# Generated by Django 2.2.28 on 2023-01-14 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vending_machine_management', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                (
                    'product',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='vending_machine_management.Product'
                    ),
                ),
                (
                    'vending_machine',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='vending_machine_management.VendingMachine'
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
