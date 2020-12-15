from django.contrib import admin
from todos import models


@admin.register(models.Todo)
class TodoAdmin(admin.ModelAdmin):
    pass

@admin.register(models.UserPost)
class TodoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'title': ('title',)}

@admin.register(models.UserComment)
class UserCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.UserLike)
class UserLikeAdmin(admin.ModelAdmin):
    pass
