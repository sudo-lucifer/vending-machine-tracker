# Generated by Django 2.2.28 on 2023-01-14 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vending_machine_management', '0005_auto_20230114_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
