from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path("", views.index, name="index"),
    path("note_add/", views.note_add, name='note_add'),
    path("note_delete/", views.note_delete, name='note_delete'),
    path("note_check/", views.note_check, name='note_check'),
]