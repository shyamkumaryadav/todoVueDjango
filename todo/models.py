import uuid
from django.db import models
from django.db import connection
from django.contrib.auth import get_user_model
from django.core.exceptions import NON_FIELD_ERRORS

User = get_user_model()


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Todo', max_length=200)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-is_done', '-date']
        unique_together = ('user', 'title', 'is_done')

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(
                cls._meta.db_table))
