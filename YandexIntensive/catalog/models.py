from django.db import models
from django.db.models import Prefetch
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import get_thumbnail, delete
from tinymce.models import HTMLField

from . import validators
from core.models import Core, CoreWithSlug


class TagsManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
                .filter(is_published=True)
                .only('name')
        )


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
    objects = TagsManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class ItemManager(models.Manager):
    def homepage_published(self):
        return (
            self.get_queryset()
                .only('name', 'category', 'text', 'tags')
                .filter(is_published=True, is_on_main=True)
                .select_related('category')
                .order_by('name')
                .prefetch_related(
                Prefetch('tags', queryset=Tag.objects.published())

            )
        )

    def item_list_published(self):
        return (
            self.get_queryset()
                .only('name', 'category', 'text', 'tags', 'photo')
                .filter(is_published=True, is_on_main=False)
                .select_related('category', 'photo')
                .order_by('category__name')
                .prefetch_related(
                Prefetch('tags', queryset=Tag.objects.published())

            )
        )


class Item(Core):
    objects = ItemManager()
    is_on_main = models.BooleanField(default=False, verbose_name="На главной")

    text = HTMLField(validators=[
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
    img = models.ImageField(upload_to='photo/%Y/%m',
                            null=True, verbose_name="Изображение",
                            help_text="Загрузите картинку")
    item = models.OneToOneField(Item, on_delete=models.CASCADE,
                                verbose_name="Товар",
                                help_text="Выберите товар")

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

    def __str__(self):
        return self.img.url

    class Meta:
        verbose_name = "Главное изображение"
        verbose_name_plural = "Главные изображения"
