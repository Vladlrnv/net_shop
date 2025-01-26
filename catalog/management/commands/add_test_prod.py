from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        products = [
            {'name': 'Пылесос', 'price': 1000},
            {'name': 'Утюг', 'price': 1000},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            self.stdout.write(self.style.SUCCESS(f'Продукт {product.name} успешно добавлен'))
