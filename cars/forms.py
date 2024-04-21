from django import forms
from cars.models import BrandsCar, Car

## CONFIGURANDO O FORMS DE FORMA MANUAL
## AQUI ESTÁ SENDO SETADO CAMPO POR CAMPO
### ESSE TRECHO DE CÓDIGO NÃO ESTÁ SENDO USADO, É APENAS DEMOSTRATIVO
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

## CONFIGURANDO O MODEL FORMS
## ELE CONFIGURA O FORMS USANDO AS CONFIGURAÇÕES DO MODEL CAR
## NO MODEL FORMS NÃO É PRECISO ESCREVER O MÉTODO SAVE()
## O MÉTODO SAVE() É NATIVO DO MODEL FORMS, LOGO ELE JÁ ESTÁ CONFIGURADO
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'