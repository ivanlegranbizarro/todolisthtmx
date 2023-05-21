from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.todos, name="todos"),
    path("add/", views.add, name="add"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("done/<int:id>/", views.done, name="done"),
]
