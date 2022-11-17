from django.db import models


class Core(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано"
    )
    name = models.CharField(
        max_length=150,
        verbose_name="Название",
        help_text="Макс 150 символов"
    )

    class Meta:
        abstract = True


class CoreWithSlug(Core):
    slug = models.SlugField(
        max_length=200,
        unique=True
    )

    class Meta:
        abstract = True
