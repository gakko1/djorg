from django.shortcuts import render
from .forms import BookmarkForm
from .models import Bookmark

def index(request):
  if request.method == 'POST':
    form = BookmarkForm(request.POST)
    if form.is_valid():
        # TODO: consider checking for request.user
        # and making this a PersonalBookmark if it exists
        form.save()
    else:
        pass  # TODO alert user that their Bookmark was invalid
  context = {}
  context['bookmarks'] = Bookmark.objects.all()
  context['form'] = BookmarkForm()  # TODO: allow editing of existing entities
  return render(request, 'bookmarks/index.html', context)
