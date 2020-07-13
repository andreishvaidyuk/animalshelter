from rest_framework import serializers

from .models import Animal


class AnimalSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=15)
    age = serializers.IntegerField()
    arrival_date = serializers.DateField()
    weight = serializers.FloatField()
    height = serializers.IntegerField()
    special_signs = serializers.CharField()

    def create(self, data):
        return Animal.objects.create(**data)

    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.age = data.get('age', instance.age)
        instance.arrival_date = data.get('arrival_date', instance.arrival_date)
        instance.weight = data.get('weight', instance.weight)
        instance.height = data.get('height', instance.height)
        instance.special_signs = data.get('special_signs', instance.special_signs)

        instance.save()
        return instance
