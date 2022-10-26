from django.http import HttpResponse


def item_detail(request, pk: int):
    return HttpResponse(f"Подробно элемент")


def item_list(request):
    return HttpResponse("Список элементов")
