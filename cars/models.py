"""This module implements class that represents the cars entity."""
import datetime

from django.db import models

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))


class Car(models.Model):
    """Cars Model"""

    class Meta(object):
        verbose_name = 'Автомобіль'
        verbose_name_plural = 'Автомобілі'

    owner = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Власник авто',)

    price = models.IntegerField(
        verbose_name='Ціна',
        null=False)

    year = models.IntegerField(
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year,
        null=False,
        verbose_name='Рік виготовлення'
        )

    BRAND_CHOICES = (
        ('Au', 'Audi'),
        ('To', 'Toyota'),
        ('Te', 'Tesla'),
        ('Po', 'Porsche')
    )
    brand = models.CharField(
        max_length=2,
        choices=BRAND_CHOICES,
        verbose_name='Марка авто',
        null=False,
        blank=False
    )

    MADE_YEAR_CHOICES = (
        ('1', 'To 1990'),
        ('2', 'From 1990 to 2000'),
        ('3', 'From 2000 to 2010'),
        ('4', 'From 2000')
    )
    category = models.CharField(
        max_length=4,
        choices=MADE_YEAR_CHOICES,
        verbose_name='категорія по року виготовлення',
        null=False,
        blank=False
    )

    MODEL_CHOICES = (
        ('audi_a6', 'Audi A6'),
        ('audi_a8', 'Audi A8'),
        ('audi_q5', 'Audi Q5'),
        ('toyota_aristo', 'Toyota Aristo'),
        ('toyota_camry', 'Toyota Camry'),
        ('tesla_model_x', 'Tesla Model X 100D Premium'),
        ('porshe_panamera', 'Porshe Panamera'),
        ('porshe_cayman', 'Porshe Cayman'),
    )
    model = models.CharField(
        max_length=20,
        choices=MODEL_CHOICES,
        null=False,
        blank=False,
        verbose_name='модель авто'
    )

    def __str__(self):
        return f'{self.get_model_display()}'
