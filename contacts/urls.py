from django.urls import path

from contacts import views

app_name = "contacts"

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("add/", views.add, name="add"),
    path("delete/<int:contact_id>/", views.delete, name="delete"),
    path("edit/<int:contact_id>/", views.edit, name="edit"),
]
