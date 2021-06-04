import datetime
from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField('Title', max_length=200)
    task = models.TextField('Description')
    publication = models.DateTimeField('Publication date')

    def __str__(self):
        return self.title

    def was_recently(self):
        return self.publication >= timezone.now() - datetime.timedelta(days=7)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    task_comment = models.ForeignKey(Task, on_delete=models.CASCADE)
    author = models.CharField('имя автора', max_length=20)
    comment_text = models.CharField("Комментарий", max_length=200)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'