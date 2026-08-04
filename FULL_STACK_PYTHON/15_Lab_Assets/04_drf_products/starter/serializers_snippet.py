# STARTER — Product serializer / API sketch
# Paste into your DRF app; finish TODOs.

from rest_framework import serializers
from .models import Product  # adjust import


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price"]

    def validate_price(self, value):
        # TODO: reject negative or zero prices with a clear error
        raise NotImplementedError
