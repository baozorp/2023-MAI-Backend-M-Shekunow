from django.contrib import admin
from games.models import Category, Game, UserProfile, UserGame


class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'rating', 'category', 'price')
    list_editable = ('price',)
    list_filter = ('category',)
    raw_id_fields = ('category',)
    search_fields = ('name', 'category')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class UserGameAdmin(admin.ModelAdmin):
    list_display = ('user', 'game')


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserGame, UserGameAdmin)
