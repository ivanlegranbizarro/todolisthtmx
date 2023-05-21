from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Todo

# Create your views here.

def todos(request):
  todos = Todo.objects.all()
  return render(request, "todo/todos.html", {"todos": todos})


@require_http_methods(["POST"])
def add(request):
  todo = None
  title = request.POST.get('title', None)

  if title:
    todo = Todo.objects.create(title=title)

  return render(request, "todo/partials/todo.html", {"todo": todo})


@require_http_methods(["POST"])
def done(request, id):
  todo = Todo.objects.get(id=id)
  todo.is_done = True
  todo.save()

  return render(request, "todo/partials/todo.html", {"todo": todo})

@require_http_methods(["POST"])
def delete(request, id):
  todo = Todo.objects.get(id=id)
  todo.delete()

  return HttpResponse()
