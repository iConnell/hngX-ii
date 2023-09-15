from django.urls import path
from .views import PersonViewsets

urlpatterns = [
    path("", PersonViewsets.as_view({"get": "list", "post": "create"}), name="person-create-list"),
    path(
        "/<int:pk>",
        PersonViewsets.as_view({"get": "retrieve", "patch": "partial_update", "delete": "destroy"}),
        name="person-retrieve-update-destroy",
    ),
]
