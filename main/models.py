from django.db import models

from users.models import User


class ToDoNote(models.Model):
    content = models.TextField(verbose_name='Запись')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_completed = models.BooleanField(default=False, verbose_name='Статус')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')

    class Meta:
        db_table = 'ToDoNote'
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return self.content