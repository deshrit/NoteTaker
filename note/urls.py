from django.urls import path
from .views import IndexView, DetailNoteView, TakeNoteView, UpdateNoteView, DeleteNoteView


app_name = "note"
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('takenote/', TakeNoteView.as_view(), name="takenote"),
    path('detailnote/<int:pk>/', DetailNoteView.as_view(), name="detailnote"),
    path('updatenote/<int:pk>/', UpdateNoteView.as_view(), name="updatenote"),
    path('deletenote/<int:pk>/', DeleteNoteView.as_view(), name="deletenote"),
]