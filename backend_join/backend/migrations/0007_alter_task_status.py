# Generated by Django 4.2.6 on 2023-10-23 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='todo', max_length=20),
        ),
    ]
