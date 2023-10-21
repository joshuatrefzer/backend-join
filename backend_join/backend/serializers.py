from rest_framework import serializers
from .models import Subtask, Task, Contact


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'

   
class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(many=True, queryset=Contact.objects.all())  # Many-to-Many-Beziehung zu Contacts
    subtasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Subtask.objects.all())  # Many-to-Many-Beziehung zu Subtasks

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        assigned_to_data = validated_data.pop('assigned_to', [])
        subtasks_data = validated_data.pop('subtasks', [])

        task = Task.objects.create(**validated_data)

        for contact in assigned_to_data:
            task.assigned_to.add(contact)

        for subtask in subtasks_data:
            task.subtasks.add(subtask)

        return task
    
    
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
        
