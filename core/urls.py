from django.urls import path
from core import views


urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.creat_todo,name='create'),
    path('todo_detail/<int:pk>/',views.detail,name='todo_detail'),
    # path('delete/<int:pk>',views.DeleteTodo.as_view(),name='delete'),
    path('delete/<int:pk>/',views.deletetodo,name='delete'),
]
