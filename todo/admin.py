import todo
from django.contrib import admin
from .models import Todo

# Add the Db create field to admin class
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created'),

# Add new admin class to Admin views
admin.site.register(Todo, TodoAdmin)