from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class Note(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  content = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  # Other fields to consider adding:
  # CharField with choices for categories
  # More sophisticated connections with Users to allow sharing
  # Hook it up to the Bookmarks
  # FileField to upload file attachments