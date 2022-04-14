from django.urls import path

from . import views

app_name = 'encyclopedia'
urlpatterns = [
    path("", views.index, name="index"),
    path("results", views.search, name="search"),
    path("add_page", views.new_page, name='new_page'),
    path("edit/<str:title>", views.edit_entry, name="edit_entry"),
    path("random", views.random, name="random"),
    path("<str:title>", views.display, name="display"),
]
