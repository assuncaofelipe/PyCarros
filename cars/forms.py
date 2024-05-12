from django import forms
from cars.models import BrandsCar, Car

## CONFIGURANDO O FORMS DE FORMA MANUAL
## AQUI ESTÁ SENDO SETADO CAMPO POR CAMPO
### ESSE TRECHO DE CÓDIGO NÃO ESTÁ SENDO USADO, É APENAS DEMOSTRATIVO
class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(BrandsCar.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    valueCar = forms.FloatField()
    photo = forms.ImageField()
    
    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
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

    ## sempre que for fazer uma validação, é importante add o clean_ antes do campo a ser validade
    ## aqui está sendo validado o campo valueCar
    ## clean_valueCar valida que o carro apenas pode ser adicionado com valor acima de 14999
    ## em seguida, todas as outras funções validam os demais campos   
    def clean_valueCar(self):
        value = self.cleaned_data.get('valueCar')
        if value < 14999:
            self.add_error('valueCar', 'Valor mínimo do carro deve ser de R$ 14.999')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Não aceitamos carros com ano de fabricação menor que 1975')
        return factory_year
    
    def clean_model_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        model_year = self.cleaned_data.get('model_year')

        if model_year <= factory_year:
            self.add_error('model_year', 'o Ano de modelo deve ser superior ao ano de frabricação')
        return model_year