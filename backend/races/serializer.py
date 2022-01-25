from rest_framework import serializers

from .models import Category, Race

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )

class CategorySerializer(serializers.ModelSerializer):
    races = RaceSerializer(many = True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "races"
        )