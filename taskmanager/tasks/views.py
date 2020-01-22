from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, Note
from .forms import TaskForm, NoteForm

@login_required
def taskList(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/list.html', {'tasks' : tasks})

@login_required
def taskView(request, id):

    task = get_object_or_404(Task, pk=id)
    new_form = NoteForm()    

    if request.method == "POST":
        old_form = NoteForm(request.POST or None)
        if old_form.is_valid():
            old_form = old_form.save(commit=False)
            old_form.fk_task = task
            old_form.save()

    notes = list(Note.objects.filter(fk_task = id))        
   
    context = {
        'task' : task,
        'notes' : notes,
        'form' : new_form,
        }
   
    return render(request, 'tasks/task.html', context)

@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            task = form.save(commit=False)
            task.done = 'fazendo'
            task.user = request.user
            task.save()
            return redirect('/')
    else:            
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form' : form})

@login_required
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)
        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form' : form, 'task' : task})     
    else:
        return render(request, 'tasks/edittask.html', {'form' : form, 'task' : task})        

@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('/')

@login_required
def changeStatus(request, id):    
    task = get_object_or_404(Task, pk=id)
    if(task.done == 'fazendo'):
        task.done = 'feito'
    else:
        task.done = 'fazendo'
    
    task.save()

    return redirect('/')