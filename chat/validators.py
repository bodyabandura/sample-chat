from django.core.exceptions import ValidationError


def ascii_only_validator(value):
    try:
        value.encode("ascii")
    except UnicodeEncodeError:
        raise ValidationError("Only ASCII characters are allowed.")
