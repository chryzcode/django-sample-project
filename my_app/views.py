from django.shortcuts import render, redirect
from .models import Note
#import the noteform
from .forms import noteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

#login_required makes sure a user is authenticated before a view

#get all the notes of the currently logged in user
@login_required(login_url='login')
def myNotesList(request):
    context = {}
    notes = Note.objects.filter(user=request.user)
    context['notes'] = notes
    return render(request, 'note-list.html', context)

#add a new note
@login_required(login_url='login')
def addNote(request):
    context = {}
    form = noteForm
    if request.method == 'POST':
        note = Note.objects.create(
            user = request.user,
            title = request.POST.get('title'),
            body = request.POST.get('body')
        )
        return redirect('view-note', pk=note.pk)
    context['form'] = form
    return render(request, 'add-note.html', context)

#edit a specific note
@login_required(login_url='login')
def editNote(request, pk):
    note = Note.objects.get(pk = pk)
    if request.user.id == note.user.id:
        form = noteForm(instance=note)
        if request.method == 'POST':
            form = noteForm(request.POST, instance=note)
            if form.is_valid():
                form.save()
                return redirect('view-note', pk=note.pk)
        context = {'form':form}
        return render(request, 'edit-note.html', context)
    return redirect('notes-list')

#view a specific note
@login_required(login_url='login')
def viewNote(request, pk):
    context = {}
    note = Note.objects.get(pk = pk)
    if request.user.id == note.user.id:
        context['note'] = note
        return render(request, 'view-note.html', context)
    return redirect('notes-list')

#delete a specific note
@login_required(login_url='login')
def deleteNote(request, pk):
    note = Note.objects.get(pk=pk)
    if request.user.id == note.user.id:
        note.delete()
        return redirect('notes-list')
    return redirect('notes-list')

##delete the logged in user account
@login_required(login_url='login')
def deleteUser(request):
    user = request.user
    user.delete()
    return redirect('login')