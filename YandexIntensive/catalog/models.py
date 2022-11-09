from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import get_thumbnail, delete

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
        validators.validate_must_be_param("превосходно", "роскошно")],
        verbose_name="Описание",
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


class Gallery(models.Model):
    upload = models.ImageField(upload_to='uploads/%Y/%m',
                               verbose_name="Изображение",
                               help_text="Загрузите картинку")
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             verbose_name="Товар")

    def __str__(self):
        return self.upload.url

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Галлерея"

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop="center", quality=51)

    def image_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}"'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'Превью'
    image_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)


class Photo(models.Model):
    img = models.ImageField(upload_to='preview/%Y/%m',
                            null=True, verbose_name="Изображение",
                            help_text="Загрузите картинку")
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True,
                                verbose_name="Товар",
                                help_text="Выберите товар")

    def __str__(self):
        return self.img.url

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    @property
    def get_img(self):
        return get_thumbnail(self.img, '300x300', crop="center", quality=51)

    def image_tmb(self):
        if self.img:
            return mark_safe(
                f'<img src="{self.get_img.url}"'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'Превью'
    image_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)
