from django.shortcuts import render, redirect
from a_cars.models import Car
from a_cars.forms import CarForm

# Aqui eu tenho uam resposta http simples.
# O Django irá retornar essa resposta quando a URL correspondente for acessada no arquivo URLs do core.
def cars_view(request):
    cars = Car.objects.all().order_by('brand', 'model')
    search = request.GET.get('search')

    if search:
        # cars = Car.objects.filter(plate__contains=search) 
        # Nesta linha, a explressão "plate__contains=search" é um filtro que busca por plates "placas", que contenham a string "search". Se fosse "model__contains=search", ele buscaria por modelos que contivessem a string "search". O mesmo vale para "brand__contains=search", que buscaria por modelo "marcas", que contivessem a string "search".

        cars = Car.objects.filter(model__icontains=search)
    return render(request, 'cars.html', {'cars': cars}) 
  

def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarForm()

    return render(request, 'new_car.html', {'new_car_form': new_car_form})

