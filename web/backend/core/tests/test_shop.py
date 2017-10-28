
"""
TestCases:
  * TeteingCreating
  * TestingDisplayable
  * TestingTimeStamped
  * TestingIndexable
"""

from django.test import TestCase

from .models import (TestOffer,
                     TestOfferPage)


class TestingCreating(TestCase):

    """
    В тесте проверятеся, может ли миксин создаваться,
    нет ли ошибок при создании
    """
    def test_offer(cls):
        TestOffer.objects.create(price=12)
        TestOffer.objects.create(price=13,
                                 name='Offer',
                                 description="OfferDescription")

    def test_offer_page(cls):
        TestOfferPage.objects.create(slug='slug_1', price=12)
        TestOfferPage.objects.create(slug='slug_2', name='Offer', price=15)

    @classmethod
    def tearDownClass(cls):
        # Удаляю всё что создал в тесте
        map(lambda model: model.objects.all().delete(),
            (TestOffer,
             TestOfferPage))
        super(TestingCreating, cls).tearDownClass()


class TestingOffer(TestCase):

    def test_is_save_on_save(cls):
        a = TestOffer(name='Offer_1',
                      price=12,
                      old_price=15)
        b = TestOffer(name='Offer_2',
                      price=15,
                      old_price=12)
        a.save()
        b.save()

        cls.assertTrue(a.is_sale)
        cls.assertFalse(b.is_sale)

        a.old_price, a.price = a.price, a.old_price
        b.old_price, b.price = b.price, b.old_price

        a.save()
        b.save()

        cls.assertTrue(b.is_sale)
        cls.assertFalse(a.is_sale)

    @classmethod
    def tearDownClass(cls):
        # Удаляю всё что создал в тесте
        TestOffer.objects.all().delete()
        super(TestingOffer, cls).tearDownClass()
