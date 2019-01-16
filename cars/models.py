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
        ('AU', 'Audi'),
        ('TY', 'Toyota'),
        ('TS', 'Tesla'),
        ('PS', 'Porsche')
    )
    brand = models.CharField(
        max_length=2,
        choices=BRAND_CHOICES,
        verbose_name='Марка авто',
        blank=False)

    MADE_YEAR_CHOICES = (
        ('1800', 'To 1990'),
        ('1990', 'From 1990 to 2000'),
        ('2000', 'From 2000 to 2010'),
        ('2010', 'From 2000')
    )
    category = models.CharField(
        max_length=4,
        choices=MADE_YEAR_CHOICES,
        verbose_name='категорія по року виготовлення',
        blank=False)

    MODEL_CHOICES = (
        ('A6', 'Audi A6'),
        ('A8', 'Audi A6'),
        ('Q5', 'Audi Q5'),
        ('Aristo', 'Toyota Aristo'),
        ('Camry', 'Touota Camry'),
        ('ModelX', 'Tesla Model X 100D Premium'),
        ('Panamera', 'Porshe Panamera'),
        ('Cayman', 'Pordhe Cayman'),
    )
    models = models.CharField(
        max_length=10,
        choices=MODEL_CHOICES,
        blank=False,
        verbose_name='молель авто')
