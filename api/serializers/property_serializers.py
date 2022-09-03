from rest_framework import serializers

from api.models import Property


class PropertySerializer(serializers.ModelSerializer):
    property_address = serializers.CharField(max_length=255, required=True)
    listing_price = serializers.IntegerField(required=True)

    class Meta:
        model = Property

        fields = ("id", "property_address", "listing_price")
