from django.db import models

class Board(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    description = models.CharField('Описание', max_length=150)

    class Meta:
        verbose_name = 'Board'
        ordering = ['name'] # Сортировка по умолчанию для всех запросов

    def __str__(self):
        return self.name
    