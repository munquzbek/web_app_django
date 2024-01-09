from django.db import models
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименования категории')
    description = models.TextField(**NULLABLE, verbose_name='Описание категории')
    created_at = models.DateTimeField(auto_now=True, verbose_name='дата создания категории')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименования')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    # category = models.CharField(max_length=100, verbose_name='Категория')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    create_date = models.DateTimeField(auto_now=True, verbose_name='дата создания')
    date_last_change = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, **NULLABLE,
                             verbose_name='Пользователь')

    def __str__(self):
        return f'{self.name}, ({self.category})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    number = models.CharField(max_length=100, verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='название версии')
    tag = models.BooleanField(default=True, verbose_name='признак версии')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
