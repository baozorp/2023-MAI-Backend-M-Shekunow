from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_view, name='main_view'),

    path('usergames', views.user_game_list, name='all_games'),

    path('categories', views.game_categories, name='game_categories'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('gcategories', views.CategoryList.as_view(), name='CategoryList'),
    path('gcategories/<int:pk>/', views.CategoryDetail.as_view(), name='CategoryDetail'),
    path('gcategories/update/<int:id>', views.CategoryUpdate.as_view(), name='CategoryUpdate'),
    path('gcategories/delete/<int:id>', views.CategoryDelete.as_view(), name='CategoryDelete'),

    path('list', views.game_list, name='all_games'),
    path('list/<int:game_id>/', views.game_detail, name='game_detail'),
    path('glist/', views.GameList.as_view(), name='GameList'),
    path('glist/<int:pk>/', views.GameDetail.as_view(), name='GameDetail'),
    path('glist/update/<int:id>', views.GameUpdate.as_view(), name='GameUpdate'),
    path('glist/delete/<int:pk>', views.GameDelete.as_view(), name='GameDelete'),


    path('profile', views.user_profile, name='profile'),
    path('profile/<int:user_id>/', views.user_profile_detail, name='user_profile_detail'),
    path('gprofile', views.UserProfileList.as_view(), name='UserProfileList'),
    path('gprofile/<int:pk>/', views.UserProfileDetail.as_view(), name='UserProfileDetail'),
    path('gprofile/update/<int:id>', views.UserProfileUpdate.as_view(), name='UserProfileUpdate'),
    path('gprofile/delete/<int:id>', views.UserProfileDelete.as_view(), name='UserProfileDelete'),
]
