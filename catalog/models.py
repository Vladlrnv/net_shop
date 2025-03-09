from django.conf import settings
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
    image = models.ImageField(upload_to='product/image', verbose_name='Изображение продукта', null=True, blank=True)
    category = models.ForeignKey(Category, models.CASCADE, verbose_name='Категория продукта', null=True, blank=True, related_name='products')
    price = models.IntegerField(verbose_name='Цена продукта')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    upload_at = models.DateField(verbose_name='Дата последнего изменения', auto_now=True)
    publication_attribute = models.BooleanField(null=True, blank=True, default=False, verbose_name="Признак публикации")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Владелец')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']
        permissions = [
            ('can_unpublish_product', 'can unpublish product',),
            ('can_delete_product', 'can delete product')
        ]

    def __str__(self):
        return f'{self.name} {self.category}'
