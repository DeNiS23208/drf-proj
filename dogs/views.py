from symtable import Class

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, ListCreateAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from dogs.models import Breed, Dog
from dogs.serializers import BreedSerializer, DogSerializer, DogDetailSerializer


class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    filterset_fields = ('breed',)
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ('date_born',)
    search_fields = ('name',)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return DogDetailSerializer
        return DogSerializer


class BreedCreateApiView(CreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedListApiView(ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedRetrieveApiView(RetrieveAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedUpdateApiView(UpdateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedDestroyApiView(DestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
