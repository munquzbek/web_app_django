import json

from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        delete_categories = Category.objects.all()
        delete_categories.delete()
        with open('data.json', 'r') as f:
            categories = json.load(f)

        for category in categories:
            print(category)
            Category.objects.create(**category['fields'])
