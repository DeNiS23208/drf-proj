from rest_framework.routers import SimpleRouter

from dogs.views import DogViewSet
from dogs.apps import DogsConfig

app_name = DogsConfig.name
router = SimpleRouter()
router.register("", DogViewSet)



urlpatterns = []

urlpatterns += router.urls