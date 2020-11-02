"""
The file defines serializers for both Dog and Breed models
The serializers are used in view.py
"""

from snippets.models import Breed, Dog
from rest_framework import serializers


class Breed_Serializer(serializers.ModelSerializer):

    """
    The class serialize all of the attributes of the Breed model
    """
    related_dogs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Breed
        fields = ['name', 'size', 'friendliness', 'trainability',
                  'sheddingamount', 'exerciseneeds', 'id', 'related_dogs']


class Dog_Serializer(serializers.ModelSerializer):

    """
    The class serialize all of the attributes of the Dog model
    """
    class Meta:
        model = Dog
        fields = ['name', 'age', 'gender', 'color', 'favoritefood',
                  'favoritetoy', 'id', 'breeds']
