from django.contrib import admin

from .models import Subtask, Task , Contact

# Register your models here.
admin.site.register(Task)
admin.site.register(Contact)
admin.site.register(Subtask)