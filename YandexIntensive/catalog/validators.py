import re

from django.core.exceptions import ValidationError


def validate_item_text(value):
    must_be_in_our_item = {"превосходно", "роскошно", }
    cleaned_string = re.sub(r'[^\w\s]', '', value)
    cleaned_value = set(cleaned_string.split())
    difference = must_be_in_our_item - cleaned_value

    if len(difference) == len(must_be_in_our_item):
        raise ValidationError(
            f"Обязательно используйте слова {must_be_in_our_item}"
        )
    return value


def validate_category_weight(value):
    if not 0 < value < 32767:
        raise ValidationError("Может принимать значение от 0 до 32767")
    return value