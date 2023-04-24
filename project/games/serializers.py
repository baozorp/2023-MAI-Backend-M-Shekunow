from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')


class GameSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = models.Game
        fields = ('id', 'name', 'release_date', 'rating', 'price', 'category')


class UserProfileSerializer(serializers.ModelSerializer):
    games = serializers.SerializerMethodField()

    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'games')

    def get_games(self, obj):
        user_games = models.UserGame.objects.filter(user=obj)
        game_ids = user_games.values_list('game_id', flat=True)
        games = models.Game.objects.filter(id__in=game_ids)
        game_serializer = GameSerializer(games, many=True)
        return game_serializer.data
