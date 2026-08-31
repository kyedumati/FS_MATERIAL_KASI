# Reference pattern
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user).order_by("-id")
    return render(request, "tasks/list.html", {"tasks": tasks})


@login_required
def task_create(request):
    form = TaskForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        task = form.save(commit=False)
        task.owner = request.user
        task.save()
        return redirect("task_list")
    return render(request, "tasks/form.html", {"form": form})
