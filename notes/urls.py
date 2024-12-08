from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),  # List view
    path('note/<int:pk>/', views.note_detail, name='note_detail'),  # Detail view
    path('create/', views.create_note, name='create_note'),  # Create view
    path('edit/<int:pk>/', views.edit_note, name='edit_note'),  # Edit view
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),  # Delete view
]
