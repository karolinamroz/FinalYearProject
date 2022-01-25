from rest_framework import serializers

from .models import Register, RegisteredRace

from races.serializer import RaceSerializer

class MyRaceItemSerializer(serializers.ModelSerializer):    
    race = RaceSerializer()

    class Meta:
        model = RegisteredRace
        fields = (
            "price",
            "race",
            "quantity",
        )

class MyRaceSerializer(serializers.ModelSerializer):
    items = MyRaceItemSerializer(many=True)

    class Meta:
        model = Register
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "place",
            "phone",
            "stripe_token",
            "items",
            "paid_amount"
        )

class RegisteredRaceSerializer(serializers.ModelSerializer):    
    class Meta:
        model = RegisteredRace
        fields = (
            "price",
            "race",
            "quantity",
        )

class RegisterSerializer(serializers.ModelSerializer):
    items = RegisteredRaceSerializer(many=True)

    class Meta:
        model = Register
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "place",
            "phone",
            "stripe_token",
            "items",
        )
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        register = Register.objects.create(**validated_data)

        for item_data in items_data:
            RegisteredRace.objects.create(register=register, **item_data)
            
        return register