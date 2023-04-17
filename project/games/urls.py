from django.urls import path
from . import views


handler405 = 'views.handler_405'
urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('categories', views.game_categories, name='game_categories'),
    path('product/<int:product_id>', views.game_product, name='game_product'),
    path('list', views.all_games, name='all_games'),
]
views.handler_405 = 'views.handler_405'
