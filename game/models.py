from django.db import models
from .validators import validate_box_size


class Box(models.Model):
    is_closed = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    code = models.CharField(max_length=20)
    owner = models.ForeignKey('authentication.CustomUser', on_delete=models.CASCADE)
    count = models.SmallIntegerField(default=1)
    size = models.SmallIntegerField(validators=[validate_box_size])