from django.db import models


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Игра')
    description = models.TextField(verbose_name='Описание')
    release_date = models.DateField(verbose_name='Дата релиза')
    rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Рейтинг')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"
        ordering = ('-rating', 'price')


class UserProfile(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(unique=True, verbose_name='Почта')
    games = models.ManyToManyField(Game, through='UserGame')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class UserGame(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Имя')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')

    def __str__(self):
        return f'{self.user.name} - {self.game.name}'

    class Meta:
        verbose_name = "Игры пользователя"
        verbose_name_plural = "Игры пользователей"
        unique_together = ('user', 'game',)
