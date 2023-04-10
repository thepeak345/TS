from django.db import models
from .validators import validate_box_size


class Box(models.Model):
    title = models.CharField(max_length=255)
    is_closed = models.BooleanField(default=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    code = models.PositiveSmallIntegerField(null=True)
    count = models.PositiveSmallIntegerField(default=1)
    size = models.PositiveSmallIntegerField(validators=[validate_box_size])
    is_active = models.BooleanField(default=True)

    def save(self, **kwargs):
        if self.count == self.size:
            self.is_active = False
        super(Box, self).save()


