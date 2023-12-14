from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Products(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='main/images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Брос'
        verbose_name_plural = 'Бро'
