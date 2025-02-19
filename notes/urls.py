from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('create/', views.create_note, name='create_note'),
    path('edit/<int:pk>/', views.edit_note, name='edit_note'),
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),
    path('manage-categories/', views.manage_categories, name='manage_categories'),
    path('edit-category/<int:category_id>/', views.edit_category, name='edit_category'), 
    path('delete-category/<int:category_id>/', views.delete_category, name='delete_category'),
]
