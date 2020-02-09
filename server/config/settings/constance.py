import os

CONSTANCE_BACKEND = 'constance.backends.redisd.RedisBackend'
CONSTANCE_REDIS_CONNECTION = os.environ.get('REDIS_URL', 'redis://redis:6379/0')
CONSTANCE_REDIS_CONNECTION_CLASS = 'django_redis.get_redis_connection'
CONSTANCE_ADDITIONAL_FIELDS = {

    'char_field': ['django.forms.CharField', {'max_length': 255}],
    'url_field': ['django.forms.URLField', {}],

}

CONSTANCE_CONFIG = {
    'CBR': ('http://www.cbr.ru/scripts/XML_daily.asp', 'Сайт ЦБ РФ', 'url_field'),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'Ссылки для парсинга': (
        'CBR',
    ),
}
