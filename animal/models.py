from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    arrival_date = models.DateField()
    weight = models.FloatField()
    height = models.IntegerField()
    special_signs = models.TextField()

    def __str__(self):
        return self.name

