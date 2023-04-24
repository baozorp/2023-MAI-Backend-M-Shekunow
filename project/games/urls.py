from django.urls import path
from . import views


handler405 = 'views.handler_405'
urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('profile', views.user_profile, name='profile'),
    path('categories', views.game_categories, name='game_categories'),
    path('usergames', views.user_game_list, name='all_games'),
    path('list', views.game_list, name='all_games'),
    path('profile/<str:user_name>/', views.specific_profile, name='specific_profile'),
]
views.handler_405 = 'views.handler_405'
