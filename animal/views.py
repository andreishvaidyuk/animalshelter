from .models import Animal
from django.views import generic


class IndexView(generic.ListView):
    context_object_name = 'latest_animal_list'
    template_name = 'animal/index.html'

    def get_queryset(self):
        return Animal.objects.all()


class DetailView(generic.DetailView):
    model = Animal
    template_name = 'animal/detail.html'


class CreateView(generic.CreateView):
    model = Animal
    fields = ['name', 'age', 'arrival_date', 'weight', 'height', 'special_signs']
    template_name = 'animal/create.html'
    success_url = '/animal/'


class DeleteView(generic.DeleteView):
    model = Animal
    success_url = '/animal/'


