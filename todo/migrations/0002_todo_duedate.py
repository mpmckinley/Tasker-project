# Generated by Django 3.1.4 on 2020-12-18 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='duedate',
            field=models.DateTimeField(null=True),
        ),
    ]
