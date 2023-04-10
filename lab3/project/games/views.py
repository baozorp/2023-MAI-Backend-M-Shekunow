from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST

# Заглушка для страницы профиля
def profile(request):
    user_profile = {
        'username': 'JohnDoe',
        'email': 'johndoe@example.com',
        'age': 25,
        'gender': 'male',
        'location': 'USA'
    }
    return JsonResponse(user_profile)

# Заглушка для страницы категорий игр
def game_categories(request):
    categories = ['Action', 'Adventure', 'RPG', 'Strategy', 'Sports', 'Simulation']
    return JsonResponse(categories, safe=False)

# Заглушка для страницы продукта
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
