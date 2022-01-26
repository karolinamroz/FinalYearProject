from rest_framework import serializers

from .models import Register, RegisteredRace


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
            "sortcode",
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