from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from .models import Category, Game, UserProfile, UserGame

from django.shortcuts import render


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


@ require_http_methods(["GET", "POST"])
def user_game_list(request):
    if request.method == 'GET':
        user_games = UserGame.objects.all().values('user_id', 'user__name', 'game_id', 'game__name')
        return JsonResponse(list(user_games), safe=False)
    else:
        return HttpResponseBadRequest('Invalid request method')
