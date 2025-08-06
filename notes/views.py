from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Category
from .forms import NoteForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from pytz import timezone as pytz_timezone
from django.db.models import Q
from django.contrib import messages

def note_list(request):
    notes = Note.objects.all()
    categories = Category.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        notes = notes.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        )
    
    # Category filter
    category_id = request.GET.get('category')
    if category_id:
        notes = notes.filter(category_id=category_id)
    
    context = {
        'notes': notes,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_id
    }
    return render(request, "notes/note_list.html", context)

def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        category_name = request.POST.get('category_name')
        if category_name:
            category.name = category_name
            category.save()
            messages.success(request, 'Category updated!')
            return redirect('manage_categories')
    return render(request, "notes/edit_category.html", {"category": category})

def manage_categories(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name')
        if category_name:
            Category.objects.create(name=category_name)
            messages.success(request, 'Category created!')
        return redirect('manage_categories')
    
    categories = Category.objects.all() 
    return render(request, "notes/manage_categories.html", {"categories": categories})

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('manage_categories')

def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            category_id = request.POST.get('category')
            if category_id:
                note.category = Category.objects.get(id=category_id)
            note.save()
            return redirect("note_list") 
    else:
        form = NoteForm()
    categories = Category.objects.all()
    return render(request, "notes/note_form.html", {
        "form": form,
        "categories": categories
    })

def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated!')
            next_url = request.POST.get('next', None)
            if next_url:
                return redirect(next_url)
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    
    categories = Category.objects.all()
    return render(request, "notes/note_form.html", {
        "form": form,
        "categories": categories
    })

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return HttpResponseRedirect(reverse("note_list"))

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    local_tz = pytz_timezone('Asia/Kathmandu')
    
    if note.created_at.tzinfo is None:
        note.created_at = timezone.make_aware(note.created_at)
    if note.updated_at.tzinfo is None:
        note.updated_at = timezone.make_aware(note.updated_at)
        
    note.created_at_local = note.created_at.astimezone(local_tz)
    note.updated_at_local = note.updated_at.astimezone(local_tz)

    return render(request, "notes/note_detail.html", {"note": note})

    # DO NOT TOUCH: TRY1 - Trigger redeployment for migrations
