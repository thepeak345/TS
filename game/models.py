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

    def save(self, **kwargs):
        if self.count == self.size:
            self.is_active = False
        super(Box, self).save()


class PairUser(models.Model):
    box = models.ForeignKey('game.Box', on_delete=models.SET_NULL, null=True)
    'user + user = 2 * user'
    pass


