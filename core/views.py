
from django.urls import reverse_lazy
from django.forms import Form
from django.shortcuts import redirect, render , get_object_or_404
from django.urls import reverse 
from django.views import generic
from .models import TodoModel
from .forms import TodoForm
from django.http import HttpResponsePermanentRedirect

# Create your views here.

def get_show_todos(request,todos):
    if request.GET and request.GET.get('filter'):
        if request.GET.get('filter')== 'yes':
            return todos.filter(is_completed= True)
        if request.GET.get('filter') =='no':
            return todos.filter(is_completed=False)    
    return todos

def index(request):
    todos = TodoModel.objects.all()
    yes = todos.filter(is_completed=True).count()
    no = todos.filter(is_completed=False).count()
    allcount = todos.count()
    return render(request,'core/index.html',{
        'todos':get_show_todos(request,todos),
        'allcount':allcount,
        'yes':yes,
        'no':no,
        })



def creat_todo(request):
    form= TodoForm()
    
    if request.method == "POST":
        todo= TodoForm(data=request.POST)
        if todo.is_valid():
            title = request.POST.get("title")
            description = request.POST.get("description")
            is_completed = request.POST.get("is_completed",False)

            todo =TodoModel()

            todo.title= title
            todo.description = description
            todo.is_completed = True if is_completed == "on" else False

            todo.save()
            # return HttpResponsePermanentRedirect(reverse('todo_detail',kwargs={'id':todo.pk}))
            return redirect('index')
    form = TodoForm()        
    return render(request,'core/create.html',{'form':form})    




def detail(request, pk):
    todos= TodoModel.objects.filter(id = pk)
    # todos = get_object_or_404(TodoModel,pk=id) 
    return render(request,'core/todo_detail.html',{'todos':todos})



def deletetodo(request, pk):
    todos = TodoModel.objects.filter(id=pk)
    if todos:
        form = todos.delete()
        return redirect('index')
    return render(request,'core/delete.html',{'form':form})
    

# class DeleteTodo(generic.DeleteView):
#     model = TodoModel
#     form_class = TodoForm
#     template_name = 'core/delete.html'

#     success_url= reverse_lazy('core:index')
    
    # def get_success_url(self):
    #     return reverse_lazy('core:index')


