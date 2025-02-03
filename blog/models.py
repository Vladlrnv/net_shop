from django.db import models


class BlogEntry(models.Model):
    header = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое', null=True, blank=True)
    preview = models.ImageField(upload_to='blogentry/image', verbose_name='Превью', null=True, blank=True)
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    publication_attribute = models.BooleanField(verbose_name='Признак публикации', default=False)
    quantity_views = models.IntegerField(verbose_name='Количество просмотров', default=0, null=True, blank=True)

    class Meta:
        verbose_name = 'Блоговая запись'
        verbose_name_plural = 'Блоговые записи'

    def __str__(self):
        return f'{self.header}'
