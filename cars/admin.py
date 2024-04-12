from django.contrib import admin
from cars.models import Car, BrandsCar

class BrandsCarAdmin(admin.ModelAdmin):
    # verificar se existe uma maneira de pegar todos os campos por meio de parametro
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    # verificar se existe uma maneira de pegar todos os campos por meio de parametro
    list_display = ('modelCar', 'brand', 'factory_year', 'modelCar_year', 'valueCar')
    search_fields = ('modelCar', 'brand')

admin.site.register(BrandsCar, BrandsCarAdmin)
admin.site.register(Car, CarAdmin)
