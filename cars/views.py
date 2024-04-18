from django.shortcuts import render
from cars.models import Car
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
    ...