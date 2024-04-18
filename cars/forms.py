from django import forms
from cars.models import BrandsCar

class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(BrandsCar.objects.all())
    factory_year = forms.IntegerField()
    modelCar_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    valueCar = forms.FloatField()
    photo = forms.ImageField()