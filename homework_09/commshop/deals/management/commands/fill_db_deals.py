from django.core.management.base import BaseCommand, CommandError
from deals.models import (
    Committent,
    DealStatus,
    Deal,
    ProductElement,
)
from products.models import ProductInstance


class Command(BaseCommand):
    help = 'Fill db'

    def handle(self, *args, **options):
        print('Стартуем')
        print('1. Удаление старых данных.')
        ProductElement.objects.all().delete()
        Deal.objects.all().delete()
        Committent.objects.all().delete()
        DealStatus.objects.all().delete()

        print("2. Создаем новый набор данных.")
        print("2.1. Создаем статусы сделок.")
        deal_open = DealStatus.objects.create(status_text='Открыта')
        deal_close = DealStatus.objects.create(status_text='Закрыта')

        print("2.2. Создаем данные коммиттентов (тек, кто принес товар на продажу).")
        committent_1 = Committent.objects.create(
            name='Иван',
            surname='Иванов',
            patronymic='Иванович',
            registration_date='06.06.2022',
        )
        committent_2 = Committent.objects.create(
            name='Петр',
            surname='Петров',
            patronymic='Петрович',
            registration_date='07.07.2022',
        )
        committent_3 = Committent.objects.create(
            name='Сергей',
            surname='Сергеев',
            patronymic='Сергеевич',
            registration_date='08.08.2022',
        )

        print("2.3. Создаем данные договоров.")
        deal_1 = Deal.objects.create(
            committent=committent_1,
            date_start='2022-06-06',
            date_close=None,
            status=deal_open,
        )
        deal_2 = Deal.objects.create(
            committent=committent_2,
            date_start='2022-07-07',
            date_close='2022-10-06',
            status=deal_close,
        )
        deal_3 = Deal.objects.create(
            committent=committent_3,
            date_start='2022-08-08',
            date_close=None,
            status=deal_open,
        )

        print("2.4. Создаем данные товара, который принес коммиттент.")
        product_instance = ProductInstance.objects.get(name='Ga-H61M-D2-B3')
        prod_elem = ProductElement.objects.create(
            prod_inst=product_instance,
            deal=deal_1,
            code_number='100001',
            price='3000',
            notes='Состояние новой.'
        )
        product_instance = ProductInstance.objects.get(name='Celeron G1610T')
        prod_elem = ProductElement.objects.create(
            prod_inst=product_instance,
            deal=deal_1,
            price='150',
            notes='Скол на кристалле. На работоспособность не влияет.'
        )
        product_instance = ProductInstance.objects.get(name='Z77M')
        prod_elem = ProductElement.objects.create(
            prod_inst=product_instance,
            deal=deal_2,
            price='4000',
            notes='Состояние новой.'
        )
        product_instance = ProductInstance.objects.get(name='Core i3-510')
        prod_elem = ProductElement.objects.create(
            prod_inst=product_instance,
            deal=deal_2,
            price='200',
            notes='Состояние новой.'
        )
        product_instance = ProductInstance.objects.get(name='WD30EFRX')
        prod_elem = ProductElement.objects.create(
            prod_inst=product_instance,
            deal=deal_3,
            price='2500',
            notes='2 бед блока'
        )
        print('3. Операции окончены')