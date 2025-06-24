from rest_framework.serializers import ModelSerializer, SerializerMethodField

from dogs.models import Breed, Dog


class BreedSerializer(ModelSerializer):
    dogs = SerializerMethodField

    def get_dogs(self, breed):
        return [dog.name for dog in Dog.object.filter(breed=breed)]
    class Meta:
        model = Breed
        fields = "__all__"


class DogSerializer(ModelSerializer):
    breed = BreedSerializer()

    class Meta:
        model = Dog
        fields = "__all__"


class DogDetailSerializer(ModelSerializer):
    count_dog_with_same_breed = SerializerMethodField()
    breed = BreedSerializer()

    def get_count_with_same_breed(self, dog):
        return Dog.objects.filter(breed=dog.breed).count()

    class Meta:
        model = Dog
        fields = ("name", "breed", "date_born", "count_dot_with_same_breed")


class BreedSerializer(ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"
