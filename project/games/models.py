from django.db import models


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class GenreGame(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.game.name} ({self.genre.name})'


class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.ManyToManyField(Genre, through=GenreGame)

    def __str__(self):
        return self.name
