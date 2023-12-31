# Generated by Django 4.2.6 on 2023-10-17 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='subtask',
            name='description',
        ),
        migrations.AddField(
            model_name='contact',
            name='first_name',
            field=models.CharField(default='default_value', max_length=30),
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default='default_value', max_length=30),
        ),
        migrations.AddField(
            model_name='subtask',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='title',
            field=models.CharField(max_length=20),
        ),
        migrations.RemoveField(
            model_name='task',
            name='subtasks',
        ),
        migrations.AddField(
            model_name='task',
            name='subtasks',
            field=models.JSONField(default=list),
        ),
    ]
