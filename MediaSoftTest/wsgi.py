"""
WSGI config for MediaSoftTest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import datetime
import os

from django.core.wsgi import get_wsgi_application

from django.contrib.auth import get_user_model
from shops.models import City, Street, Shop

User = get_user_model()

if not User.objects.filter(email='admin@admin.ru').exists():
    admin = User.objects.create_superuser('admin', 'admin@admin.ru', 'admin')

    cities = [
        City(city_name='Ульяновск'),
        City(city_name='Москва'),
        City(city_name='Санкт-Петербург'),
    ]

    City.objects.bulk_create(cities)

    streets = [Street(street_name='Гончарова', city=cities[0]),
               Street(street_name='Среднеохтинский проспект', city=cities[2]),
               Street(street_name='Ленина', city=cities[1]),
               Street(street_name='Брантовская Дорога', city=cities[2]),
               ]
    Street.objects.bulk_create(streets)

    shops = [
        Shop(shop_name='Лента Охта-Молл', street=streets[-1], city=cities[2], home='3А', open_time=datetime.time(0, 0),
             close_time=datetime.time(23, 59)),
        Shop(shop_name='Мини Лента', street=streets[-1], city=cities[2], home='3к1', open_time=datetime.time(8, 0),
             close_time=datetime.time(22, 0)),
        Shop(shop_name='Гуливер', street=streets[0], city=cities[0], home='1', open_time=datetime.time(8, 0),
             close_time=datetime.time(22, 0)),
        Shop(shop_name='1337 Store', street=streets[2], city=cities[1], home='1337', open_time=datetime.time(0, 0),
             close_time=datetime.time(1, 0)),
    ]

    Shop.objects.bulk_create(shops)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MediaSoftTest.settings')

application = get_wsgi_application()
