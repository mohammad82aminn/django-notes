from django.urls import path

from . import views

app_name = "notes"

urlpatterns = [
    path("", views.notes_list_view, name="list"),
]