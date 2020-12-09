from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-is_done', '-date']
        unique_together = ('user', 'title')
