from django.db import models
from django.utils.timezone import now
import pytz

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['order', 'name']  # Order categories by custom order, then alphabetically

class Note(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)      # Automatically set on update
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        # If no title is provided, set the title to a more readable date and time format in the local timezone
        if not self.title:
            local_tz = pytz.timezone('Asia/Kathmandu')
            now_in_local_tz = now().astimezone(local_tz)
            self.title = now_in_local_tz.strftime('%d %b %Y - %I:%M %p, %a')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
