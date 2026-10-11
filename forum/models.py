from django.db import models
from django.conf import settings


class Board(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    description = models.CharField('Описание', max_length=150)

    class Meta:
        ordering = ['name'] # Сортировка по умолчанию для всех запросов

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField('Заголовок', max_length=255)
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        related_name='topics',      # board.topics.all()
        verbose_name='Раздел',
        )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='topics',      # user.topics.all()
        verbose_name='Автор',
    )
    created_at = models.DateTimeField('Создана', auto_now_add=True) # только при создании
    views = models.PositiveBigIntegerField('Просмотры', default=0)

    class Meta:
        ordering = ['-created_at'] # новые сверху

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField('Сообщение', max_length=4000)
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name='posts',
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='posts',
    )
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Изменено', auto_now=True) # при каждом save()

    class Meta:
        ordering = ['created_at'] # старые сверху

    def __str__(self):
        return self.message[:50]