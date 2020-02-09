from django.contrib import admin

from apps.parser.models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    readonly_fields = ['date']
