from django import forms  
from a_cars.models import Car, Brand

# forma antiga e mais demorada para se usar form.
class CarForm(forms.Form):
    model = forms.CharField(max_length=200, label='Modelo')
    brand = forms.ModelChoiceField(Brand.objects.all(), label='Marca')   # Quando for chave estrangeira, usar ModelChoiceField.
    factory_year = forms.IntegerField(label='Ano')
    mode_year = forms.IntegerField(label='Ano do modelo')
    plate = forms.CharField(max_length=10, label='Placa')
    value = forms.FloatField(label='Valor')
    photo = forms.ImageField(label='Imagem', required=False)

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            mode_year = self.cleaned_data['mode_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],            
            photo = self.cleaned_data['photo'],
        )
        car.save()
        return car

# Moo produtivo para criar forms.
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        # Podria ser assim:
        # fields = ['model', 'brand', 'factory_year', 'mode_year', 'plate', 'value', 'photo']
      
        # Mas usarei o recuro "__all__" para pegar todos os campos.
        fields = '__all__'

        # Lembrando que no modo anterior, foi preciso indicar o campo brand como chave estrangeira manualmente.
        # Aqui, o Django já faz isso automaticamente.
        # 
  
