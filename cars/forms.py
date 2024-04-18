from django import forms
from cars.models import BrandsCar, Car

class CarForm(forms.Form):
    modelCar = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(BrandsCar.objects.all())
    factory_year = forms.IntegerField()
    modelCar_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    valueCar = forms.FloatField()
    photo = forms.ImageField()
    
    def save(self):
        car = Car(
            modelCar = self.cleaned_data['modelCar'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            modelCar_year = self.cleaned_data['modelCar_year'],
            plate = self.cleaned_data['plate'],
            valueCar = self.cleaned_data['valueCar'],
            photo = self.cleaned_data['photo'],
        )
        car.save()
        return car