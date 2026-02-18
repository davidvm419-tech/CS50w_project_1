from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search_query, name="search_query"),
    path("newPage", views.newPage, name="newPage"),
    path("wiki/<str:title>/editEntry", views.editEntry, name="editEntry"),
    path("randomEntry", views.randomEntry, name="randomEntry"),
    ]
