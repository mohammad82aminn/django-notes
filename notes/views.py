from django.shortcuts import render
from . import models


def notes_list_view(request):
    notes = models.Note.objects.all()
    context = {
        "note_list" : notes
    }
    return render(request, 'notes/notes_list.html', context)





# Create your views here.
