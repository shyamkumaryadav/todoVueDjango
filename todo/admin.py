from django.contrib import admin
from .models import Todo
from django.contrib.auth import get_user_model
User = get_user_model()

admin.site.site_header = "Todo Admin"
admin.site.site_title = "Todo Admin app"
admin.site.index_title = "Welcome to Todo app"


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_done', 'date')
    list_filter = ('is_done', 'date')
    # filter_horizontal = ('user')
    date_hierarchy = 'date'
    search_fields = ['title']
    readonly_fields = ('id', )
    fields = ['id', 'user', ('title', 'is_done')]