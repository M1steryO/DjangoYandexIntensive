from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.item_list),
    re_path(r'(?<![-.])\b(?P<pk>[1-9][0-9]*)\b(?!\.[0-9])', views.item_detail)
]
