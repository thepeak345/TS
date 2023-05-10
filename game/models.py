from django.db import models
from .validators import validate_box_size


class Box(models.Model):
    title = models.CharField('Название', max_length=255)
    is_closed = models.BooleanField('Закрыта', default=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    code = models.PositiveSmallIntegerField(null=True)
    count = models.PositiveSmallIntegerField(default=1)
    size = models.PositiveSmallIntegerField('Количество игроков', validators=[validate_box_size])
    is_active = models.BooleanField(default=True)


class Pair(models.Model):
    player1 = models.ForeignKey('authentication.CustomUser', on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey('authentication.CustomUser', on_delete=models.CASCADE, related_name='player2')
    box = models.ForeignKey('game.Box', on_delete=models.CASCADE)
