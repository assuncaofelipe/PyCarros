from cars.models import Car
from cars.forms import CarModelForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    # realiza buscars no db
    def get_queryset(self):
        queryset_Cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            queryset_Cars = queryset_Cars.filter(Q(model__icontains=search) | 
                                                 Q(brand__name__icontains=search))
        return queryset_Cars

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars'