from django.shortcuts import render

from catalog.models import Item, Photo


def home(request):
    template_name = 'homepage/index.html'
    items = Item.objects.homepage_published()
    photos = Photo.objects.select_related('item')
    context = {'active': 'home',
               'items': items,
               'photos': photos}
    return render(request, template_name, context)
