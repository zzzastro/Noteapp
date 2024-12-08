from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from pytz import timezone as pytz_timezone


def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new note to the database
            return redirect("note_list")  # Redirect to the list of notes
    else:
        form = NoteForm()  # Display an empty form for GET requests

    return render(request, "notes/note_form.html", {"form": form})


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)  # Get the note by primary key

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()  # Save the changes to the note
            
            # Get the 'next' parameter (the URL to redirect to after saving)
            next_url = request.POST.get('next', None)
            
            if next_url:
                return redirect(next_url)  # Redirect to the detail page or wherever the 'next' URL is
            else:
                return redirect("note_list")  # If no 'next' URL, go to the list page

    else:
        form = NoteForm(instance=note)  # Pre-populate the form with existing note data

    return render(request, "notes/note_form.html", {"form": form})


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)  # Get the note by primary key
    note.delete()  # Delete the note from the database
    return HttpResponseRedirect(reverse("note_list"))  # Redirect to the note list page


def note_list(request):
    notes = Note.objects.all()  # Get all notes
    return render(request, "notes/note_list.html", {"notes": notes})


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    local_tz = pytz_timezone('Asia/Kathmandu')  # Your local timezone
    # Ensure created_at and updated_at are timezone-aware
    if note.created_at.tzinfo is None:
        note.created_at = timezone.make_aware(note.created_at)
    if note.updated_at.tzinfo is None:
        note.updated_at = timezone.make_aware(note.updated_at)
    # Convert created_at and updated_at to local time
    note.created_at_local = note.created_at.astimezone(local_tz)
    note.updated_at_local = note.updated_at.astimezone(local_tz)

    return render(request, "notes/note_detail.html", {"note": note})
