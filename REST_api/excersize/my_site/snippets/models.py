"""
This file defines models to be used in the site
"""

from django.db import models


class Breed(models.Model):

    """
    A model class with attributes representing a dog's qualities
    The class also has an __str__ method which represent some attributes nicely
    """
    size_choices = [('Tiny', 'Tiny'), ('Small', 'Small'), ('Medium', 'Medium'),
                    ('Large', 'Large')]
    range_choices = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    name = models.CharField(max_length=20)
    size = models.CharField(max_length=7, choices=size_choices)
    friendliness = models.IntegerField(choices=range_choices)
    trainability = models.IntegerField(choices=range_choices)
    sheddingamount = models.IntegerField(choices=range_choices)
    exerciseneeds = models.IntegerField(choices=range_choices)

    def __str__(self):
        return self.name


class Dog(models.Model):

    """
    A model class with attributes representing a breed's qualities
    The class also has an __str__ method which represent some attributes nicely
    """
    breeds = models.ForeignKey(Breed, related_name='related_dogs',
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    favoritefood = models.CharField(max_length=10)
    favoritetoy = models.CharField(max_length=10)

    def __str__(self):
        return self.name
