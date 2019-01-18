from django.db.models.signals import pre_save
from django.dispatch import receiver

from cars.models import Car


@receiver(pre_save, sender=Car)
def my_callback(sender, instance, *args, **kwargs):
    if instance.year < 1990:
        instance.category = '1'
    elif instance.year >=1990 and instance.year < 2000:
        instance.category = '2'
    elif instance.year >=2000 and instance.year < 2010:
        instance.category = '3'
    else:
        instance.category = '4'
