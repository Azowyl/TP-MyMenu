from rest_framework import serializers

from MyMenu.apps.menu.models import Dish


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'