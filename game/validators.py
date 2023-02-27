from django.core.exceptions import ValidationError


def validate_box_size(value):
    if value % 2 != 0:
        raise ValidationError(
            "Количество игроков должно быть четным",
            params={"value": value}
        )
