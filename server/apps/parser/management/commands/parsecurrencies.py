from django.core.management.base import BaseCommand

from apps.parser.utils import _parse_currencies


class Command(BaseCommand):
    def handle(self, *args, **options):
        _parse_currencies()
