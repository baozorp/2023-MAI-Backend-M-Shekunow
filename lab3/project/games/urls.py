from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('categories', views.game_categories, name='game_categories'),
    path('product/<int:product_id>', views.game_product, name='game_product'),
]
