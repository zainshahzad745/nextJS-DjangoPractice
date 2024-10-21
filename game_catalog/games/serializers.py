from rest_framework import serializers
from .models import Platform, Category, Game

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class GameSerializer(serializers.ModelSerializer):
    platform = PlatformSerializer()  # To show platform details in the game response
    category = CategorySerializer(many=True)  # Many-to-many relationship

    class Meta:
        model = Game
        fields = ['id', 'title', 'description', 'release_date', 'platform', 'category', 'cover_image', 'created_by']
