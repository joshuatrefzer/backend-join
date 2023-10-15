from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=30, default='default_value')
    last_name = models.CharField(max_length=30, default='default_value')
    mail = models.EmailField()
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Subtask(models.Model):
    title = models.CharField(max_length=100, default=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)  # Die Zuweisung erfolgt an ein Contact-Objekt
    date = models.DateField()
    prio = models.CharField(max_length=10)
    category = models.CharField(max_length=20)
    subtasks = models.ManyToManyField('Subtask', blank=True)

    def __str__(self):
        return self.title

