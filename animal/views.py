from .models import Animal
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# представление для отображения приветствия
class GreetingView(generic.TemplateView):
    template_name = 'animal/greeting.html'


# представление для отображения списка животных
class IndexView(generic.ListView):
    context_object_name = 'latest_animal_list'
    template_name = 'animal/index.html'

    def get_queryset(self):
        return Animal.objects.all()


# представление для отображения деталей по выбранному животному
class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Animal
    template_name = 'animal/detail.html'


# представление для отображения формы создания нового животного в базе
class CreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Animal
    fields = ['name', 'age', 'arrival_date', 'weight', 'height', 'special_signs']
    template_name = 'animal/create.html'
    success_url = '/animal/index'
    permission_required = 'animal.add_animal'


# представление для удаления выбранного животного
class DeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Animal
    success_url = '/animal/index'
    permission_required = 'animal.delete_animal'


