from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание категории', null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название продукта')
    description = models.TextField(verbose_name='Описание продукта', null=True, blank=True)
    image = models.ImageField(upload_to='catalog/image', verbose_name='Изображение продукта', null=True, blank=True)
    category = models.ForeignKey(Category, models.CASCADE, verbose_name='Категория продукта', null=True, blank=True, related_name='products')
    price = models.IntegerField(verbose_name='Цена продукта')
    created_at = models.DateField(verbose_name='Дата создания', null=True, blank=True, auto_now_add=True)
    upload_at = models.DateField(verbose_name='Дата последнего изменения', null=True, blank=True, auto_now=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']

    def __str__(self):
        return f'{self.name} {self.category}'
