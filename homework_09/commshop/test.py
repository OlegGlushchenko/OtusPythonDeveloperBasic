from django.test import TestCase
from django.contrib.auth.models import User
from products.models import (
    ProductCategory,
    ProductInstance,
    PropertyType,
    PropertyInstance,
)
from deals.models import (
    Committent,
    DealStatus,
    Deal,
    ProductElement,
)


# Create your tests here.
class TestDealsModels(TestCase):

    def setUp(self) -> None:
        cat_motherboard = ProductCategory.objects.create(category_name='motherboard')

        motherboard = ProductInstance.objects.create(
            name='Ga-H61M-D2-B3',
            category=cat_motherboard,
        )

        deal_open = DealStatus.objects.create(status_text='Открыта')
        committent = Committent.objects.create(
            name='Иван',
            surname='Иванов',
            patronymic='Иванович',
            registration_date='06.06.2022',
        )
        deal = Deal.objects.create(
            committent=committent,
            date_start='2022-06-06',
            date_close=None,
            status=deal_open,
        )
        prod_elem = ProductElement.objects.create(
            prod_inst=motherboard,
            deal=deal,
            code_number='100001',
            price='3000',
            notes='Состояние новой.'
        )
        self.cat_motherboard = cat_motherboard
        self.motherboard = motherboard
        self.deal_open = deal_open
        self.committent = committent
        self.deal = deal
        self.prod_elem = prod_elem

    def tearDown(self) -> None:
        ProductElement.objects.get(id=self.prod_elem.id).delete()
        ProductInstance.objects.get(id=self.motherboard.id).delete()
        ProductCategory.objects.get(id=self.cat_motherboard.id).delete()
        Deal.objects.get(id=self.deal.id).delete()
        Committent.objects.get(id=self.deal_open.id).delete()
        DealStatus.objects.get(id=self.committent.id).delete()

    def test_model_deal_committent(self):
        self.assertEqual(self.deal.committent.name, 'Иван')

    def test_model_deal_status(self):
        self.assertEqual(self.deal.status.status_text, 'Открыта')


class TestDealsViews(TestCase):

    def test_response_status_code(self):
        response = self.client.get('/deals/')
        self.assertEqual(response.status_code, 200)

    def test_response_context_unidentified(self):
        response = self.client.get('/deals/')
        self.assertIn('identification', response.context)
        self.assertEqual(response.context['identification'], 'Гость')

    def test_response_context_identified(self):
        user = User.objects.create_superuser(username='admin', email='admin@email.com', password='admin')
        self.client.login(username='admin', password='admin')
        response = self.client.get('/deals/')
        self.assertIn('identification', response.context)
        self.assertEqual(response.context['identification'], user.username)

    def test_deal_detail_404(self):
        response = self.client.get('/deals/000/')
        self.assertEqual(response.status_code, 404)

    def test_deal_detail(self):
        cat_motherboard = ProductCategory.objects.create(category_name='motherboard')

        motherboard = ProductInstance.objects.create(
            name='Ga-H61M-D2-B3',
            category=cat_motherboard,
        )

        deal_open = DealStatus.objects.create(status_text='Открыта')
        committent = Committent.objects.create(
            name='Иван',
            surname='Иванов',
            patronymic='Иванович',
            registration_date='06.06.2022',
        )
        deal = Deal.objects.create(
            committent=committent,
            date_start='2022-06-06',
            date_close=None,
            status=deal_open,
        )
        product_instance = motherboard
        prod_elem = ProductElement.objects.create(
            prod_inst=product_instance,
            deal=deal,
            code_number='100001',
            price='3000',
            notes='Состояние новой.'
        )

        response = self.client.get(f'/deals/{deal.pk}')
        self.assertEqual(response.status_code, 200)


class TestProductsModels(TestCase):

    def setUp(self) -> None:
        cat_motherboard = ProductCategory.objects.create(category_name='motherboard')
        motherboard = ProductInstance.objects.create(
            name='Z77M',
            category=cat_motherboard,
        )
        mb_manufacturer = PropertyType.objects.create(
            name='Производитель',
            type='Строка',
            prod_cat=cat_motherboard,
        )
        product = PropertyInstance.objects.create(
            prod_inst=motherboard,
            prod_type=mb_manufacturer,
            value='Asrock',
        )
        self.cat_motherboard = cat_motherboard
        self.motherboard = motherboard
        self.mb_manufacturer = mb_manufacturer
        self.product = product

    def tearDown(self) -> None:
        PropertyInstance.objects.get(id=self.product.id).delete()
        PropertyType.objects.get(id=self.mb_manufacturer.id).delete()
        ProductInstance.objects.get(id=self.motherboard.id).delete()
        ProductCategory.objects.get(id=self.cat_motherboard.id).delete()

    def test_model_product(self):
        self.assertEqual(self.motherboard.name, 'Z77M')

    def test_model_product_category(self):
        self.assertEqual(self.motherboard.category.category_name, 'motherboard')


class TestProductsViews(TestCase):

    def test_response_status_code(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_deal_detail_404(self):
        response = self.client.get('/products/000/')
        self.assertEqual(response.status_code, 404)

    def test_deal_detail(self):
        cat_motherboard = ProductCategory.objects.create(category_name='motherboard')
        product = ProductInstance.objects.create(
            name='Z77M',
            category=cat_motherboard,
        )

        response = self.client.get(f'/products/{product.pk}')
        self.assertEqual(response.status_code, 200)
