# TODO: private tasks per user — paste into your Django app

"""Starter patterns for Lab 06 / Forms+Auth.

Copy into your project and replace NotImplemented bits.
"""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render, redirect


class Task(models.Model):
    title = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self) -> str:
        return self.title


# forms.py idea:
# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ["title", "is_done"]


@login_required
def task_list(request):
    # TODO: filter tasks so only request.user sees their rows
    raise NotImplementedError("Filter Task.objects by owner=request.user")


@login_required
def task_create(request):
    # TODO: on valid POST, save with owner=request.user (commit=False pattern)
    raise NotImplementedError("Create Task owned by the logged-in user")
