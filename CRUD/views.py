from django.shortcuts import render, redirect
from .models import ToDo
from .forms import TodoForm
# Create your views here.


def Todo_view(request):
    form=TodoForm()
    if request.method == 'POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_url')
    template_name='app1/Todo.html'
    context={'form':form}
    return render(request, template_name, context)

def display(request):
    obj=ToDo.objects.all()
    template_name='app1/display.html'
    context={'obj':obj}
    return render(request, template_name, context)

def update_view(request,pk):
    obj=ToDo.objects.get(id=pk)
    form=TodoForm(instance=obj)
    if request.method == 'POST':
        form=TodoForm(request.POST,instance=obj)
        form.save()
        return redirect('display_url')
    template_name='app1/todo.html'
    context={'form':form}
    return render(request, template_name, context)

def delete_view(request,pk):
    template_name='app1/confirmation.html'
    if request.method == 'POST':
        obj = ToDo.objects.get(id=pk)
        obj.delete()
        return redirect('display_url')
    context={}
    return render(request, template_name, context)

'''

def home_view(request):
    template_name='app1/base.html'
    context={}
    return render(request, template_name, context)
'''


