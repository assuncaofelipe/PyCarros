# Generated by Django 5.0.4 on 2024-05-11 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_carinvetory_alter_car_plate'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='bio',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
