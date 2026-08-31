# BROKEN — both users see all tasks
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Task


@login_required
def task_list(request):
    # Bug: no owner filter
    tasks = Task.objects.all()
    return render(request, "tasks/list.html", {"tasks": tasks})


@login_required
def task_create(request):
    # Bug: form saved without setting owner
    ...
