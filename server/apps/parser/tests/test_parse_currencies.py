from django.core.management import call_command
from django.test import TestCase
from apps.parser.models import Currency

CBR_CURRENCIES_COUNT = 34


class ParseCurrenciesTestCase(TestCase):
    def test_mycommand(self):
        args = []
        opts = {}
        call_command('parsecurrencies', *args, **opts)
        self.assertEqual(Currency.objects.count(), CBR_CURRENCIES_COUNT)
