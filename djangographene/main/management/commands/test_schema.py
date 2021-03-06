import json
from django.core.management.base import BaseCommand

from main.schema import result


class Command(BaseCommand):
    help = 'tests_schema'

    def handle(self, *args, **options):
        items = dict(result.data.items())
        print(json.dumps(items, indent=4))