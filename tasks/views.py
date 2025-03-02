from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def HomeView(request):
    tasks = Task.objects.all().order_by('-pk')
    return render(request, 'todo.html', {'tasks': tasks})

def TaskCreate(request):
    if request.method == 'POST':
        name = request.POST['name']
        task = Task.objects.create(name=name)
        task.save()
        print('task created...')
    return redirect('home')

def TaskUpdate(request,pk):
    task = Task.objects.get(pk=pk)
    if task.is_done == False:
         task.is_done = True
         task.save()
         return redirect('home')
    else:
        task.is_done = False
        task.save()
        return redirect('home')
        