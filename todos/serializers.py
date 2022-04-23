from dataclasses import field
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

    def create(self, validated_data):
        # Getting user from request
        user = self.context.get("request").user
        # If the request contains a valid user then it adds it as the owner of the to the todo object, otherwise owner is Null
        if user is not None:
            todo = Todo.objects.create(**validated_data)
            todo.owner = user
            todo.save()
            return todo
        return super().create(validated_data)
