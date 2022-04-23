from django.urls import path
from .views import TodoDetail, TodoList

urlpatterns = [
    path('todos/', TodoList.as_view(), name='todos'),
    path('todos/<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
]
