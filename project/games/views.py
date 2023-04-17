from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from .models import Category, Game, UserProfile, UserGame

# View for the game categories page


@require_http_methods(["GET", "POST"])
def game_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all().values('id', 'name')
        return JsonResponse(list(categories), safe=False)
    elif request.method == 'POST':
        # Process POST request to create a new category
        pass
    else:
        return HttpResponseBadRequest('Invalid request method')

# View for the game list page


@require_http_methods(["GET", "POST"])
def game_list(request):
    if request.method == 'GET':
        games = Game.objects.all().values('id', 'name', 'release_date', 'rating', 'price', 'category__name')
        return JsonResponse(list(games), safe=False)
    elif request.method == 'POST':
        # Process POST request to create a new game
        pass
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


def specific_profile(request, user_name):
    if request.method == 'GET':
        user = UserProfile.objects.filter(name__icontains=user_name).values('id', 'name', 'email')
        return JsonResponse(list(user), safe=False)
    else:
        return HttpResponseBadRequest('Invalid request method')

# View for the user's game list page


@ require_http_methods(["GET", "POST"])
def user_game_list(request, user_id):
    if request.method == 'GET':
        user_games = UserGame.objects.filter(user_id=user_id).values('game_id', 'game__name', 'game__description', 'game__release_date', 'game__rating', 'game__price', 'game__category__name')
        return JsonResponse(list(user_games), safe=False)
    elif request.method == 'POST':
        # Process POST request to add a game to user's list
        pass
    else:
        return HttpResponseBadRequest('Invalid request method')
