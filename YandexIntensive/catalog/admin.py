from django.contrib import admin

from .models import Item, Category, Tag, Gallery, Photo


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class GalleryInLine(admin.StackedInline):
    model = Gallery


class PhotoInLine(admin.StackedInline):
    model = Photo
    extra = 1
    max_num = 1


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published", "is_on_main", "image_tmb")
    list_editable = ("is_published", "is_on_main")
    list_display_links = ("name",)
    filter_horizontal = ('tags',)
    inlines = [GalleryInLine, PhotoInLine, ]

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.img = None
