from django.urls import path  # type: ignore[reportMissingModuleSource]

from inventory import views

urlpatterns = [
    path("", views.item_list, name="item_list"),
    path("delete/<int:item_id>/", views.delete_item, name="delete_item"),
]