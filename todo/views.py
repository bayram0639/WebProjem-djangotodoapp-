from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import TodoApp
# Create your views here.
def index(request):
    todos = TodoApp.objects.all()
    return render(request,"index.html", {"todos":todos})

def addTodoApp(request):
    if request.method == "GET":
        return redirect("/")

    else: 
        title = request.POST.get("title") 
        newTodoApp = TodoApp(title=title,completed=False)

        newTodoApp.save()
        return redirect("/")     

def update(request,id):
    todo = get_object_or_404(TodoApp, id=id)
    todo.completed = not todo.completed

    todo.save()
    return redirect("/")

def delete(request,id):    
    todo = get_object_or_404(TodoApp, id=id)
    
    todo.delete()
    return redirect("/")          