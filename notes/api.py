from rest_framework import serializers, viewsets
from .models import Note

# Serializers define the API representation

class NoteSerializer(serializers.HyperlinkedModelSerializer):
  """Serializer to define the API representation for Notes."""

  class Meta:
    model = Note
    fields = ('title', 'content')


class NoteViewSet(viewsets.ModelViewSet):
  """ViewSet to define the view behavior for Notes."""

  serializer_class = NoteSerializer
  queryset = Note.objects.all()