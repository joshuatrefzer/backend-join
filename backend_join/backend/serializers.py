from rest_framework import serializers
from .models import Task, Contact, Subtask



class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        def create(self, validated_data):
            subtasks_data = validated_data.pop('subtasks')
            task = Task.objects.create(**validated_data)
            for subtask_data in subtasks_data:
                Subtask.objects.create(task=task, **subtask_data)
            return task
        
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
        
