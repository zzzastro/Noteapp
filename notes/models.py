from django.db import models
from django.utils.timezone import now
import pytz

class Note(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)  # Allow title to be optional
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)      # Automatically set on update

    def save(self, *args, **kwargs):
        # If no title is provided, set the title to a more readable date and time format in the local timezone
        if not self.title:
            local_tz = pytz.timezone('Asia/Kathmandu')  # Replace with your local timezone
            now_in_local_tz = now().astimezone(local_tz)  # Convert current time to local timezone
            self.title = now_in_local_tz.strftime('%d %b %Y - %I:%M %p, %a')  # Format: "27 Nov 2024 - 03:40 PM, Wed"
        super().save(*args, **kwargs)  # Call the original save method
