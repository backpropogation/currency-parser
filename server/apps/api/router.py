from rest_framework.routers import DefaultRouter

from apps.api.viewsets import CurrencyViewSet

router = DefaultRouter()
router.register('currencies', CurrencyViewSet, base_name='currency')
