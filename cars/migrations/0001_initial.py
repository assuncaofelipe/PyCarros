# Generated by Django 5.0.4 on 2024-04-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('modelCar', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('factory_year', models.IntegerField(blank=True, null=True)),
                ('modelCar_year', models.IntegerField(blank=True, null=True)),
                ('valueCar', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
