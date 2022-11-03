from django.db import models

from . import validators
from core.models import Core, CoreWithSlug


class Category(CoreWithSlug):
    weight = models.IntegerField(default=100, validators=[
        validators.validate_category_weight,
    ])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(CoreWithSlug):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Item(Core):
    text = models.TextField(validators=[
        validators.validate_item_text,
    ], verbose_name="Описание",
        help_text='Описание должно быть больше,'
                  'чем из 2х слов и содержать слова "превосходно, роскошно" ')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name="Категория",
                                 help_text="Выберете категорию")
    tags = models.ManyToManyField(Tag, verbose_name="Tags")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
