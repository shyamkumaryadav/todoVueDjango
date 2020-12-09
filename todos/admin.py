from django.contrib import admin
from todos.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
