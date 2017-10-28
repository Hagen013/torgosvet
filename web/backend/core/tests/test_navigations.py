
"""
TestCases:
  * TeteingCreating
  * TestingDisplayable
  * TestingTimeStamped
  * TestingIndexable
"""

from django.test import TestCase

from .models import (TestCategoryPage)


class TestingTestCategoryPage(TestCase):

    @classmethod
    def setUpTestData(cls):
        root = TestCategoryPage(slug="")
        root.save()
        a = TestCategoryPage(slug="a", parent=root)
        a.save()
        b = TestCategoryPage(slug="b", parent=root)
        b.save()
        a_a = TestCategoryPage(slug="a_a", parent=a)
        a_a.save()
        b_a = TestCategoryPage(slug="b_a", parent=b)
        b_a.save()
        b_b = TestCategoryPage(slug="b_b", parent=b)
        b_b.save()

    def test_get_url(cls):
        # у рута урл
        cls.assertEqual(TestCategoryPage.objects.get(slug="").get_url(),
                        "")
        # у первого уровня
        cls.assertEqual(TestCategoryPage.objects.get(slug="a").get_url(),
                        "a/")
        # у следующих
        cls.assertEqual(TestCategoryPage.objects.get(slug="b_a").get_url(),
                        "b/b_a/")

    @classmethod
    def tearDownClass(cls):
        # Удаляю всё что создал в тесте
        TestCategoryPage.objects.all().delete()
        super(TestingTestCategoryPage, cls).tearDownClass()
