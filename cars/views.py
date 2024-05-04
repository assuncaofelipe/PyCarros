from cars.models import Car
from cars.forms import CarModelForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    # realiza buscars no db
    def get_queryset(self):
        queryset_Cars = super().get_queryset().order_by('modelCar')
        search = self.request.GET.get('search')
        if search:
            queryset_Cars = queryset_Cars.filter(Q(modelCar__icontains=search) | 
                                                 Q(brand__name__icontains=search))
        return queryset_Cars
    
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars'