from django import forms
from .models import Note
from datetime import datetime

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        # Do not set the title by default in the __init__ method, leave it empty initially
        if not self.instance.pk and not self.instance.title:
            self.instance.title = ''  # Ensure it's empty initially

    def clean_title(self):
        title = self.cleaned_data.get('title')

        # If title is empty, auto-generate the title (uppercase date and time)
        if not title:
            title = datetime.now().strftime("%b %d, %Y - %I:%M %p, %a").upper()

        return title
