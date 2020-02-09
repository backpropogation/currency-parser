import random

from django.contrib.auth.models import User
from django.core.management import call_command
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from apps.parser.models import Currency


class CurrenciesApiTestCase(APITestCase):
    def set_credentials(self):
        self.user = User.objects.create_user(username='root123', password='123')
        self.token = Token.objects.get_or_create(user=self.user)[0]
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

    def test_get_currencies_without_credentials(self):
        url = reverse('currency-list')
        response = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_get_currency_without_credentials(self):
        url = reverse('currency-detail', args=(1,))
        response = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_get_currencies_with_credentials(self):
        self.set_credentials()
        call_command('parsecurrencies')
        url = reverse('currency-list')
        response = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_currency_with_credentials(self):
        self.set_credentials()
        call_command('parsecurrencies')
        url = reverse(
            'currency-detail',
            args=(
                random.choice(Currency.objects.values_list('id', flat=True)),
            )
        )
        response = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
