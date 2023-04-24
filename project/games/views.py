from django.http import JsonResponse, HttpResponseBadRequest

from django.views.decorators.http import require_http_methods
from .models import Category, Game, UserProfile, UserGame
from rest_framework import generics
from django.shortcuts import render, get_object_or_404
from . import serializers


def main_view(request):
    return render(request, 'main_template.html', {})


# View for the game categories page


@require_http_methods(["GET", "POST"])
def game_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all().values('id', 'name')
        return JsonResponse(list(categories), safe=False)
    else:
        return HttpResponseBadRequest('Invalid request method')

# View for the game list page


@require_http_methods(["GET", "POST"])
def game_list(request):
    if request.method == 'GET':
        games = Game.objects.all().values('id', 'name', 'release_date', 'rating', 'price', 'category__name')
        return JsonResponse(list(games), safe=False)
    else:
        return HttpResponseBadRequest('Invalid request method')

# View for the user profile page


@require_http_methods(["GET", "POST"])
def user_profile(request):
    if request.method == 'GET':
        user = UserProfile.objects.all().values('id', 'name', 'email')
        return JsonResponse(list(user), safe=False)
    else:
        return HttpResponseBadRequest('Invalid request method')


@require_http_methods(["GET", "POST"])
def specific_profile(request, user_name):
    if request.method == 'GET':
        user = UserProfile.objects.filter(name__icontains=user_name).values('id', 'name', 'email')
        return JsonResponse(list(user), safe=False)
    else:
        return HttpResponseBadRequest('Invalid request method')

# View for the user's game list page


@require_http_methods(["GET", "POST"])
def user_game_list(request):
    if request.method == 'GET':
        user_games = UserGame.objects.all().values('user_id', 'user__name', 'game_id', 'game__name')
        return JsonResponse(list(user_games), safe=False)
    else:
        return HttpResponseBadRequest('Invalid request method')


@require_http_methods(['GET'])
def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    serializer = serializers.GameSerializer(game)
    return JsonResponse(serializer.data)


@require_http_methods(['GET'])
def user_profile_detail(request, user_id):
    user_profile = get_object_or_404(UserProfile, id=user_id)
    serializer = serializers.UserProfileSerializer(user_profile)
    return JsonResponse(serializer.data)


@require_http_methods(['GET'])
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    serializer = serializers.CategorySerializer(category)
    return JsonResponse(serializer.data)

# Класс-вьюшка для получения списка всех объектов Category


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

# Класс-вьюшка для получения детального описания конкретного объекта Category по id


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

# Класс-вьюшка для обновления конкретного объекта Category по id


class CategoryUpdate(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_url_kwarg = 'id'

# Класс-вьюшка для удаления конкретного объекта Category по id


class CategoryDelete(generics.DestroyAPIView):
    queryset = Category.objects.all()
    lookup_url_kwarg = 'id'

# Класс-вьюшка для получения списка всех объектов Game


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = serializers.GameSerializer

# Класс-вьюшка для получения детального описания конкретного объекта Game по id


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = serializers.GameSerializer


class GameUpdate(generics.UpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = serializers.GameSerializer
    lookup_url_kwarg = 'id'

# Класс-вьюшка для удаления конкретного объекта Game по id


class GameDelete(generics.DestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = serializers.UserProfileSerializer

# Класс-вьюшка для получения списка всех объектов UserProfile


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer

# Класс-вьюшка для получения детального описания конкретного объекта UserProfile по id


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer

# Класс-вьюшка для обновления конкретного объекта UserProfile по id


class UserProfileUpdate(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    lookup_url_kwarg = 'id'

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

# Класс-вьюшка для удаления конкретного объекта UserProfile по id


class UserProfileDelete(generics.DestroyAPIView):
    queryset = UserProfile.objects.all()
    lookup_url_kwarg = 'id'
