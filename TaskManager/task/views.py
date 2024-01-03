from typing import Any
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,TemplateView
from django.views.generic.edit import CreateView,FormView,UpdateView,DeleteView
from . models import TaskModel
from . forms import TaskForm
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return redirect('tasklist')

    
class TaskFormView(CreateView):
    model=TaskModel
    template_name='addTask.html'
    form_class=TaskForm
    success_url=reverse_lazy('tasklist')
    
class TaskListView(ListView):
    model=TaskModel
    template_name='tasklist.html'
    context_object_name='tasks'
    
class UpdateTaskListView(UpdateView):
    model=TaskModel
    form_class=TaskForm
    template_name='addTask.html'
    success_url=reverse_lazy('tasklist')
    
class DeleteTaskView(DeleteView):
    model=TaskModel
    success_url=reverse_lazy('tasklist')
    
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
class DeleteCompletedTaskView(DeleteView):
    model=TaskModel
    success_url=reverse_lazy('completedtask')
    
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
class ComepletedTaskListView(ListView):
    model=TaskModel
    template_name='completedTask.html'
    context_object_name='tasks'
    
def taskComeplete(request,pk):
    task=get_object_or_404(TaskModel, id=pk)
    task.is_completed= True
    task.save()
    return redirect ('completedtask')

class About(TemplateView):
    template_name='about.html'
    