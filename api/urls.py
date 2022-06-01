from django.urls import path
from .views import TodoDetail, TodoListCreate

urlpatterns = [
    path('todos/', TodoListCreate.as_view(), name='todo_list_create'),
    path('todos/<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
]
