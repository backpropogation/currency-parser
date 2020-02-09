from django.db import models


class Currency(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Валюта'
    )
    rate = models.DecimalField(
        max_digits=6,
        decimal_places=4,
        verbose_name='Курс к рублю'
    )
    date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    def __str__(self):
        return self.name
