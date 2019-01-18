from django.db.models import Max, Min
from django.shortcuts import render

from cars.models import Car


def cars_list(request):
    cars = Car.objects.all()
    cars_years = cars.aggregate(Min('year'), Max('year'))
    order_by = request.GET.get('order_by', '')
    res = request.GET.get('years', '')
    if order_by in ('id', 'owner', 'price', 'year', 'brand', 'model', 'category'):
        cars = cars.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            cars = cars.reverse()
    if res:
        res = res.split(',')
        from_year = int(res[0])
        to_year = int(res[1])
        cars = cars.filter(year__gte=from_year, year__lte=to_year)

    return render(
        request,
        'cars/cars_list.html',
        {
            'cars': cars,
            'cars_years': cars_years,
            'res': res
        }
    )






