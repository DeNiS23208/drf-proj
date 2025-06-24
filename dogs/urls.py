from django.urls import path
from rest_framework.routers import SimpleRouter

from dogs.apps import DogsConfig
from dogs.views import (BreedCreateApiView, BreedDestroyApiView,
                        BreedListApiView, BreedRetrieveApiView,
                        BreedUpdateApiView, DogViewSet)

app_name = DogsConfig.name
router = SimpleRouter()
router.register("", DogViewSet)

urlpatterns = [
    path("Breeds/", BreedListApiView.as_view(), name="breeds_list"),
    path("Breeds/<int:pk>", BreedRetrieveApiView.as_view(), name="breeds_retrieve"),
    path("Breeds/create/", BreedCreateApiView.as_view(), name="breeds_create"),
    path(
        "Breeds/<int:pk>/delete/", BreedDestroyApiView.as_view(), name="breeds_delete"
    ),
    path("Breeds/<int:pk>/update/", BreedUpdateApiView.as_view(), name="breeds_update"),
]

urlpatterns += router.urls
