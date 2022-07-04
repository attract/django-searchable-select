from django.urls import re_path

from . import views

urls = [
    re_path('^filter$', views.filter_models, name='searchable-select-filter'),
]

urlpatterns = urls
