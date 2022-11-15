from django.shortcuts import render

from catalog.models import Item


def home(request):
    template_name = 'homepage/index.html'
    items = Item.objects.homepage_published()
    context = {'active': 'home',
               'items': items}
    return render(request, template_name, context)
