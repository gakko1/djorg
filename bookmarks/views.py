from django.shortcuts import render
from .models import Bookmark
from .models import BookmarkForm

def index(request):
  context = {}
  context['bookmarks'] = Bookmark.objects.all()
  return render(request, 'bookmarks/index.html', context)

def bookmark_new(request):
  form = BookmarkForm()
  return render(request, 'bookmarks/bookmarkform.html', {'form': form})
