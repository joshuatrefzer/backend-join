# Generated by Django 4.2.6 on 2023-11-13 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_alter_task_subtasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='prio',
            field=models.CharField(choices=[('urgent', 'Dringend'), ('medium', 'Medium'), ('low', 'Niedrig')], default='medium', max_length=10),
        ),
    ]
