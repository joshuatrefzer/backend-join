from rest_framework import serializers
from .models import Task, Contact




   
class TaskSerializer(serializers.ModelSerializer):
        class Meta:
            model = Task
            fields = '__all__'

        def create(self, validated_data):
            # Wenn Subtasks in den validierten Daten vorhanden sind, extrahiere sie
            subtasks_data = validated_data.pop('subtasks', [])
            
            # Erstelle den Task
            task = Task.objects.create(**validated_data)
            
            # Erstelle die zugehörigen Subtasks
            for subtask_data in subtasks_data:
                # Hier gehst du davon aus, dass Subtasks im JSON-Format sind
                # Wenn die Datenstruktur variiert, passe dies entsprechend an
                task.subtasks.append(subtask_data)

            return task
        
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
        
