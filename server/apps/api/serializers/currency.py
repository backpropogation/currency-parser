from rest_framework import serializers

from apps.parser.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Currency
        exclude = ('id',)
