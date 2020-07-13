from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import Animal
from .serializers import AnimalSerializer


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


class AnimalView(APIView):
    def get(self, request):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response({'animals': serializer.data})

    def post(self, request):
        animal = request.data.get('animal')
        serializer = AnimalSerializer(data=animal)
        if serializer.is_valid(raise_exception=True):
            animal_saved = serializer.save()
        return Response({"success": "Животное '{}' сохранено".format(animal_saved.name)})

    def put(self, request, pk):
        saved_animal = get_object_or_404(Animal.objects.all(), pk=pk)
        data = request.data.get('animal')
        serializer = AnimalSerializer(instance=saved_animal, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            animal_saved = serializer.save()
        return Response({"success": "Животное '{}' обновлено".format(animal_saved.name)})

    def delete(self, request, pk):
        animal = get_object_or_404(Animal.objects.all(), pk=pk)
        animal.delete()
        return Response({'message': "Животное с id {} удалено".format(pk)}, status=204)
