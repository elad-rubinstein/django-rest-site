"""
The file defines list and detail views for both Dog and Breed models
"""

from rest_framework.views import APIView
from snippets.models import Breed, Dog
from snippets.serializers import Dog_Serializer, Breed_Serializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response


class DogList(mixins.ListModelMixin, mixins.CreateModelMixin,
              generics.GenericAPIView):

    """
    The class contains get and post functions for dogs
    """
    queryset = Dog.objects.all()
    serializer_class = Dog_Serializer

    def get(self, request, *args, **kwargs):

        """
        The function return all existing dogs serialized into a json form
        The function also replace each Breed's id with the Breed's name
        :param request: a GET request from the user.
        :return: a json response of serialized data.
        """
        self.obj = self.list(request, *args, **kwargs)
        for index in range(len(self.obj.data)):
            breed_id = self.obj.data[index]['breeds']
            self.obj.data[index]['breeds'] = Breed.objects.get(pk=breed_id).name
        return Response(self.obj.data)

    def post(self, request, *args, **kwargs):

        """
        The function post a new dog according to the user's request
        :param request: a POST request from the user.
        :return: a json response of serialized data.
        """
        return self.create(request, *args, **kwargs)


class DogDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                mixins.DestroyModelMixin, generics.GenericAPIView):

    """
    The class contains get, retrieve and put functions for a specific dog
    """
    queryset = Dog.objects.all()
    serializer_class = Dog_Serializer

    def get(self, request, *args, **kwargs):

        """
        The function return a specific dog serialized into a json form
        :param request: a GET request from the user.
        :return: a json response of serialized data.
        """
        self.obj = self.retrieve(request, *args, **kwargs)
        return Response(self.obj.data)

    def put(self, request, *args, **kwargs):

        """
        The function update an existing dog according to the user's request
        :param request: a PUT request from the user.
        :return: a json response of serialized data.
        """
        self.obj = self.update(request, *args, **kwargs)
        return Response(self.obj.data)

    def delete(self, request, *args, **kwargs):
        """
        The function delete an existing dog according to the user's request
        :param request: a DELETE request from the user.
        :return: a json response of the deleted serialized data.
        """
        return self.destroy(request, *args, **kwargs)


class BreedList(mixins.ListModelMixin, mixins.CreateModelMixin,
                generics.GenericAPIView):

    """
    The class contains get and post functions for breeds
    """
    queryset = Breed.objects.all()
    serializer_class = Breed_Serializer

    def get(self, request, *args, **kwargs):

        """
        The function return all existing breeds serialized into a json form
        The function also adds a related_dogs and old_amount_of_related_dogs
        attributes for every breed
        :param request: a GET request from the user.
        :return: a json response of serialized data.
        """
        self.obj = self.list(request, *args, **kwargs)
        for index in range(len(self.obj.data)):
            count = 0
            lst = self.obj.data[index]["related_dogs"]
            for num in lst:
                if Dog.objects.get(pk=num).age > 10:
                    count += 1
                lst[lst.index(num)] = f"name: {Dog.objects.get(pk=num).name}" \
                                      f", id: {num}"
            self.obj.data[index]["related_dogs"] = lst
            self.obj.data[index]['old_amount_of_related_dogs'] = count
        return Response(self.obj.data)

    def post(self, request, *args, **kwargs):

        """
        The function post a new breed according to the user's request
        :param request: a POST request from the user.
        :return: a json response of serialized data.
        """
        return self.create(request, *args, **kwargs)


class BreedDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin, generics.GenericAPIView):

    """
    The class contains get, retrieve and put functions for a specific breed
    """
    queryset = Breed.objects.all()
    serializer_class = Breed_Serializer

    def get(self, request, *args, **kwargs):

        """
        The function return a specific breed serialized into a json form
        The function also adds a related_dogs and old_amount_of_related_dogs
        attributes for the breed
        :param request: a GET request from the user.
        :return: a json response of serialized data.
        """
        self.obj = self.retrieve(request, *args, **kwargs)
        lst = self.obj.data["related_dogs"]
        count = 0
        for num in lst:
            if Dog.objects.get(pk=num).age > 10:
                count += 1
            lst[lst.index(num)] = f"name: {Dog.objects.get(pk=num).name}," \
                                  f" id: {num}"
        self.obj.data["related_dogs"] = lst

        self.obj.data['old_amount_of_related_dogs'] = count
        return Response(self.obj.data)

    def put(self, request, *args, **kwargs):

        """
        The function update an existing breed according to the user's request
        The function also adds a related_dogs and old_amount_of_related_dogs
        attributes for the breed
        :param request: a PUT request from the user.
        :return: a json response of serialized data.
        """
        self.obj = self.update(request, *args, **kwargs)
        lst = self.obj.data["related_dogs"]
        count = 0
        for num in lst:
            if Dog.objects.get(pk=num).age > 10:
                count += 1
            lst[lst.index(num)] = f"name: {Dog.objects.get(pk=num).name}," \
                                  f" id: {num}"
        self.obj.data["related_dogs"] = lst

        self.obj.data['old_amount_of_related_dogs'] = count
        return Response(self.obj.data)

    def delete(self, request, *args, **kwargs):
        """
        The function delete an existing breed according to the user's request
        :param request: a DELETE request from the user.
        :return: a json response of the deleted serialized data.
        """
        return self.destroy(request, *args, **kwargs)
