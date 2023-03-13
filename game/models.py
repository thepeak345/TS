from django.db import models
from .validators import validate_box_size


class Box(models.Model):
    title = models.CharField(max_length=255)
    is_closed = models.BooleanField(default=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    code = models.SmallIntegerField(null=True)
    count = models.SmallIntegerField(default=1)
    size = models.SmallIntegerField(validators=[validate_box_size])
