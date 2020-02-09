from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from apps.api.filters import CurrenciesFilter
from apps.api.serializers import CurrencySerializer
from apps.parser.models import Currency


class CurrenciesSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Currency.objects.order_by('-date')
    serializer_class = CurrencySerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CurrenciesSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CurrenciesFilter
