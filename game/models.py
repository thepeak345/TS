from django.db import models
from .validators import validate_box_size


class Box(models.Model):
    is_closed = models.BooleanField(default=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    code = models.SmallIntegerField()
    member = models.ForeignKey(
        'authentication.CustomUser',
        on_delete=models.CASCADE,
        null=True
    )
    is_owner = models.BooleanField(default=False)
    count = models.SmallIntegerField(default=1)
    size = models.SmallIntegerField(validators=[validate_box_size])
