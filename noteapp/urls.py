from django.contrib import admin
from django.urls import path, include
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include('notes.urls')),
    path('', views.note_list, name='home'),  # Set the root URL to point to the note list view
    path("__reload__/", include("django_browser_reload.urls")),
]
