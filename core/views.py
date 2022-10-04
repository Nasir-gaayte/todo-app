
from multiprocessing import context
from django.forms import Form
from django.shortcuts import redirect, render 
from django.urls import reverse
from django.views import generic
from .models import TodoModel
from .forms import TodoForm
from django.http import HttpResponsePermanentRedirect

# Create your views here.



def index(request):
    todos = TodoModel.objects.all()
    yes = todos.filter(is_completed=True).count()
    no = todos.filter(is_completed=False).count()
    allcount = todos.count()
    return render(request,'core/index.html',{
        'todos':todos,
        'allcount':allcount,
        'yes':yes,
        'no':no,
        })



def creat_todo(request):
    form = TodoForm()
    
    if request.method == "POST":
        todo= TodoForm(request.POST)
        if todo.is_valid():
            title = request.POST.get("title")
            description = request.POST.get("description")
            is_completed = request.POST.get("is_completed",False)

            todo =TodoModel()

            todo.title= title
            todo.description = description
            todo.is_completed = True if is_completed == "on" else False

            todo.save()
            return HttpResponsePermanentRedirect(reverse('todo_detail',kwargs={'id':todo.pk}))
    return render(request,'core/create.html',{'form':form})    




def detail(request, pk):
    todos= TodoModel.objects.filter(id = pk)
    return render(request,'core/todo_detail.html',{'todos':todos})



