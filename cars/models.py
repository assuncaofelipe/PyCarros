from django.db import models

class BrandsCar(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    modelCar = models.CharField(max_length=200)
    brand = models.ForeignKey(BrandsCar, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    modelCar_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True)
    valueCar = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True) # config para diretório de mídia

    def __str__(self):
        return self.modelCar
    

