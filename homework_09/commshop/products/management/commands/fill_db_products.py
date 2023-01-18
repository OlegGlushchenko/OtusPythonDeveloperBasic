from django.core.management.base import BaseCommand
from products.models import (
    ProductCategory,
    ProductInstance,
    PropertyType,
    PropertyInstance,
)


class Command(BaseCommand):
    help = 'Fill db'

    def handle(self, *args, **options):
        print('Стартуем')
        print('1. Удаление старых данных.')
        PropertyInstance.objects.all().delete()
        PropertyType.objects.all().delete()
        ProductInstance.objects.all().delete()
        ProductCategory.objects.all().delete()

        print("2. Создаем новый набор данных.")
        print("2.1. Создаем категории товаров.")
        cat_hdd = ProductCategory.objects.create(category_name='HDD')
        cat_ssd = ProductCategory.objects.create(category_name='SSD')
        cat_cpu = ProductCategory.objects.create(category_name='CPU')
        cat_gpu = ProductCategory.objects.create(category_name='GPU')
        cat_ram = ProductCategory.objects.create(category_name='RAM')
        cat_motherboard = ProductCategory.objects.create(category_name='motherboard')

        print("2.2. Создаем данные экземляров товаров.")
        motherboard_1 = ProductInstance.objects.create(
            name='Ga-H61M-D2-B3',
            category=cat_motherboard,
        )
        motherboard_2 = ProductInstance.objects.create(
            name='Z77M',
            category=cat_motherboard,
        )
        cpu_1 = ProductInstance.objects.create(
            name='Celeron G1610T',
            category=cat_cpu,
        )
        cpu_2 = ProductInstance.objects.create(
            name='Core i3-510',
            category=cat_cpu,
        )
        hdd_1 = ProductInstance.objects.create(
            name='WD30EFRX',
            category=cat_hdd,
        )

        print("2.3. Создаем типы свойств товаров.")
        hdd_capacity = PropertyType.objects.create(
            name='Объем',
            type='Число',
            prod_cat=cat_hdd,
        )
        hdd_manufacterer = PropertyType.objects.create(
            name='Производитель',
            type='Строка',
            prod_cat=cat_hdd,
        )
        hdd_interface = PropertyType.objects.create(
            name='Интерфейс',
            type='Строка',
            prod_cat=cat_hdd,
        )
        cpu_freq = PropertyType.objects.create(
            name='Частота',
            type='Число',
            prod_cat=cat_cpu,
        )
        cpu_socket = PropertyType.objects.create(
            name='Сокет',
            type='Строка',
            prod_cat=cat_cpu,
        )
        mb_manufacturer = PropertyType.objects.create(
            name='Производитель',
            type='Строка',
            prod_cat=cat_motherboard,
        )
        mb_socket = PropertyType.objects.create(
            name='Сокет',
            type='Строка',
            prod_cat=cat_motherboard,
        )
        mb_desc = PropertyType.objects.create(
            name='Описание',
            type='Текст',
            prod_cat=cat_motherboard,
        )

        print("2.4. Создаем экземпляры свойств товаров.")
        product = PropertyInstance.objects.create(
            prod_inst=motherboard_1,
            prod_type = mb_manufacturer,
            value='GigaByte',
        )
        product = PropertyInstance.objects.create(
            prod_inst=motherboard_1,
            prod_type = mb_socket,
            value='Socket 1155',
        )
        product = PropertyInstance.objects.create(
            prod_inst=motherboard_1,
            prod_type = mb_desc,
            text_value='Бла бла бла бла......',
        )
        product = PropertyInstance.objects.create(
            prod_inst=motherboard_2,
            prod_type = mb_manufacturer,
            value='Asrock',
        )
        product = PropertyInstance.objects.create(
            prod_inst=motherboard_2,
            prod_type = mb_socket,
            value='Socket 1155',
        )
        product = PropertyInstance.objects.create(
            prod_inst=motherboard_2,
            prod_type = mb_desc,
            text_value='Бла бла бла бла......',
        )
        product = PropertyInstance.objects.create(
            prod_inst=cpu_1,
            prod_type = cpu_freq,
            value='2,3',
        )
        product = PropertyInstance.objects.create(
            prod_inst=cpu_1,
            prod_type = cpu_socket,
            value='1155',
        )
        product = PropertyInstance.objects.create(
            prod_inst=cpu_2,
            prod_type = cpu_freq,
            value='2,93',
        )
        product = PropertyInstance.objects.create(
            prod_inst=cpu_2,
            prod_type = cpu_socket,
            value='1156',
        )
        product = PropertyInstance.objects.create(
            prod_inst=hdd_1,
            prod_type = hdd_capacity,
            value='3 TB',
        )
        product = PropertyInstance.objects.create(
            prod_inst=hdd_1,
            prod_type = hdd_manufacterer,
            value='Western Digital',
        )
        product = PropertyInstance.objects.create(
            prod_inst=hdd_1,
            prod_type = hdd_interface,
            value='SATA',
        )
        print('3. Операции окончены')
