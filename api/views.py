from select import select
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from todos.models import Todo
from todos.serializers import TodoSerializer


class TodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user
        queryset = Todo.objects.all()
        if user is not None:
            queryset = queryset.filter(owner=user.id)

        return queryset


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
