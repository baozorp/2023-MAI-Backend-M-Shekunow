# Generated by Django 4.2 on 2023-04-17 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ('-rating', 'price'), 'verbose_name': 'Игра', 'verbose_name_plural': 'Игры'},
        ),
        migrations.AlterModelOptions(
            name='usergame',
            options={'verbose_name': 'Игры пользователя', 'verbose_name_plural': 'Игры пользователей'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Игра'),
        ),
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='game',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateField(verbose_name='Дата релиза'),
        ),
        migrations.AlterField(
            model_name='usergame',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game', verbose_name='Игра'),
        ),
        migrations.AlterField(
            model_name='usergame',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.userprofile', verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterUniqueTogether(
            name='usergame',
            unique_together={('user', 'game')},
        ),
    ]
