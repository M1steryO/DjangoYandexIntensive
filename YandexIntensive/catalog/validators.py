import functools
import re

from django.core.exceptions import ValidationError


def validate_category_weight(value):
    if not 0 < value < 32767:
        raise ValidationError("Может принимать значение от 0 до 32767")
    return value


def validate_must_be_param(*args):
    @functools.wraps(validate_must_be_param)
    def func(value):
        must_be_in_our_item = set(args)
        html_cleaned_string = re.sub(r"<[^>]+>", "", value, flags=re.S)
        punctuation_cleaned_string = re.sub(r'[^\w\s]', '',
                                            html_cleaned_string)

        cleaned_value = set(punctuation_cleaned_string.split())
        difference = must_be_in_our_item - cleaned_value

        if len(difference) == len(must_be_in_our_item):
            raise ValidationError(
                f"Обязательно используйте слова {must_be_in_our_item}"
            )
        return value

    return func
