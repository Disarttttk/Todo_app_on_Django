from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path("", views.index, name="index"),
    path("note_delete/", views.note_delete, name='note_delete')
]