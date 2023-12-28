# serializers.py
from rest_framework import serializers
from .models import GroceryItem

class GroceryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryItem
        fields = '__all__'

    def create(self, validated_data):
        # Convert the 'name' field to lowercase before saving
        validated_data['name'] = validated_data['name'].lower()

        # Call the default create method to save the data to the database
        return super(GroceryItemSerializer, self).create(validated_data)
