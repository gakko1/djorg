from django.shortcuts import render
from .models import Bookmark
from .forms import PostForm

def index(request):
  context = {}
  context['bookmarks'] = Bookmark.objects.all()
  return render(request, 'bookmarks/index.html', context)

def post_new(request):
  form = PostForm()
  return render(request, 'bookmarks/postform.html', {'form': form})
