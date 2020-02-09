from django_filters import rest_framework as filters


class CurrenciesFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    date_lt = filters.DateFilter(field_name="date", lookup_expr='lte')
    date_gt = filters.DateFilter(field_name="date", lookup_expr='gte')
