from django.http import JsonResponse, HttpResponseBadRequest

from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST
from django.http import HttpResponseNotAllowed
# Заглушка для страницы профиля


@require_http_methods(["GET", "POST"])
def profile(request):
    user_profile = {
        'username': 'JohnDoe',
        'email': 'johndoe@example.com',
        'age': 25,
        'gender': 'male',
        'location': 'USA'
    }
    return JsonResponse(user_profile)


@require_http_methods(["GET", "POST"])
def all_games(request):
    games = [
        {
            'title': 'Game 1',
            'category': 'Action',
            'price': 19.99
        },
        {
            'title': 'Game 2',
            'category': 'Adventure',
            'price': 29.99
        },
        {
            'title': 'Game 3',
            'category': 'RPG',
            'price': 39.99
        },
        {
            'title': 'Game 4',
            'category': 'Strategy',
            'price': 49.99
        },
        {
            'title': 'Game 5',
            'category': 'Sports',
            'price': 59.99
        },
        {
            'title': 'Game 6',
            'category': 'Simulation',
            'price': 69.99
        },
    ]
    return JsonResponse(games, safe=False)

# Заглушка для страницы категорий игр


@require_http_methods(["GET", "POST"])
def game_categories(request):
    if request.method == 'POST':
        categories = ['Action', 'Adventure', 'RPG', 'Strategy', 'Sports', 'Simulation']
        return JsonResponse(categories, safe=False)
    else:
        return HttpResponseBadRequest('Invalid request method "GET"')

# Заглушка для страницы продукта


@require_http_methods(["GET", "POST"])
def game_product(request, product_id):
    product_info = {
        'id': product_id,
        'name': 'Sample Game',
        'category': 'Action',
        'price': 10.99,
        'description': 'A sample game for demonstration purposes.',
        'release_date': '2022-01-01',
        'publisher': 'Sample Publisher',
        'developer': 'Sample Developer',
        'platforms': ['Windows', 'macOS', 'Linux'],
        'image_url': 'https://example.com/sample_game.jpg',
    }
    return JsonResponse(product_info)
