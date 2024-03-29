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
    weight = models.IntegerField(
        default=100,
        validators=[validators.validate_category_weight, ]
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Tag(CoreWithSlug):
    objects = TagsManager()

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


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
            .filter(is_published=True)
            .select_related('category', 'photo')
            .order_by('category__name')
            .prefetch_related(
                Prefetch('tags', queryset=Tag.objects.published())

            )
        )


class Item(Core):
    is_on_main = models.BooleanField(
        default=False,
        verbose_name="На главной",
    )

    text = HTMLField(
        validators=[
            validators.validate_must_be_param("превосходно", "роскошно"),
        ],
        verbose_name="Описание",
        help_text='Описание должно быть больше,'
                  'чем из 2х слов и содержать слова "превосходно, роскошно" ')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Выберете категорию"
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name="Tags"
    )

    objects = ItemManager()

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

    def image_tmb(self):
        image = Photo.objects.get(item=self.id).img

        def get_img(img):
            return get_thumbnail(
                img,
                '300x300',
                crop="center",
                quality=51
            )

        if image:
            return mark_safe(
                f'<img src="{get_img(image).url}"'
            )
        return 'No image'

    image_tmb.short_description = 'Preview'
    image_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)


class Gallery(models.Model):
    upload = models.ImageField(
        upload_to='uploads/%Y/%m',
        verbose_name="Изображение",
        help_text="Загрузите картинку"
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name="Товар"
    )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Галлерея"

    def __str__(self):
        return self.upload.url

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)


class Photo(models.Model):
    img = models.ImageField(
        upload_to='photo/%Y/%m',
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите картинку"
    )
    item = models.OneToOneField(
        Item, on_delete=models.CASCADE,
        verbose_name="Товар",
        help_text="Выберите товар"
    )

    class Meta:
        verbose_name = "Главное изображение"
        verbose_name_plural = "Главные изображения"

    def __str__(self):
        return self.img.url

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)
