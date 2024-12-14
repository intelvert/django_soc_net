from django.core.exceptions import ValidationError
import re

def username_validator(value):
    if not re.match(r'^[a-zA-Z0-9_-]+$', value):
        raise ValidationError("Username can only contain letters, numbers, underscores and hyphen.")