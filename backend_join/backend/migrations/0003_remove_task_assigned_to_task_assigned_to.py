# Generated by Django 4.2.6 on 2023-10-17 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_remove_contact_full_name_remove_subtask_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assigned_to',
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_to',
            field=models.ManyToManyField(blank=True, to='backend.contact'),
        ),
    ]
