from django.shortcuts import redirect, render
from cars.models import Car
from cars.forms import CarForm
from django.db.models import Q

def cars_view(request):
    cars = Car.objects.all().order_by('modelCar')
    search = request.GET.get('search')
    
    if search:
        cars = cars.filter(
            Q(modelCar__icontains=search) | Q(brand__name__icontains=search)
        )

    return render( 
        request,
        'cars.html',
        {'cars': cars}
    )

def new_car_view(request):
    if request.method.upper() == 'POST':
        new_car_form = CarForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarForm()
    return render(
            request, 
            'new_car.html', 
            { 'new_car_form': new_car_form }
        )
    