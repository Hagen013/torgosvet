"""
TestCases:
 * TeteingCreating
 * TestingDisplayable
 * TestingTimeStamped
 * TestingIndexable
"""

from django.test import TestCase

from .models.base import (TestDescribable,
                          TestDisplayable,
                          TestTimeStamped,
                          TestIndexable,
                          TestNamed,
                          TestWebPage
                          )

from .models.base import (TestDisplayableNotImplemented,)


class TestingCreating(TestCase):

    """
    В тесте проверятеся, может ли миксин создаваться,
    нет ли ошибок при создании
    """
    def test_describable(cls):
        TestDescribable.objects.create()
        TestDescribable.objects.create(description="Тут Описание и прочее")

    def test_displayable(cls):
        TestDisplayable.objects.create()
        TestDisplayable.objects.create(slug="slug1")
        TestDisplayable.objects.create(slug="slug2", is_published=True)
        TestDisplayable.objects.create(slug="slug3", is_published=False)
        TestDisplayable.objects.create(slug="slug4",
                                       is_published=True,
                                       scoring=10)

    def test_timestamped(cls):
        TestTimeStamped.objects.create()
        TestTimeStamped().save(auto_now=False)
        TestTimeStamped().save()

    def test_indexable(cls):
        TestIndexable.objects.create()

    def test_named(cls):
        TestNamed.objects.create()
        TestNamed.objects.create(name="Name1")

    def test_web_page(cls):
        TestWebPage.objects.create(slug="slug0")
        TestWebPage.objects.create(slug="slug1")
        TestWebPage.objects.create(slug="slug2",
                                   description="Тут Описание и прочее")

    def test_displayable_get_url_not_implemented(cls):
        cls.assertRaises(NotImplementedError,
                         TestDisplayableNotImplemented.objects.create
                         )
        cls.assertRaises(NotImplementedError,
                         TestDisplayableNotImplemented().get_url
                         )

    def test_displayable_get_absolute_url_not_implemented(cls):
        cls.assertRaises(NotImplementedError,
                         TestDisplayableNotImplemented().get_absolute_url
                         )

    @classmethod
    def tearDownClass(cls):
        # Удаляю всё что создал в тесте
        map(lambda model: model.objects.all().delete(),
            (TestDescribable,
            TestDisplayable,
            TestTimeStamped,
            TestIndexable,
            TestNamed,
            TestWebPage))
        super(TestingCreating, cls).tearDownClass()


class TestingDisplayable(TestCase):

    """
    Displayable
     * Тест работы get_url()
     * Тест работы get_absolute_url()
     * Тест работы менеджера public
    """
    test_data = [
        # SLUG | SCOR | IS_PUBLISHED
        ['slug1', 8, True],
        ['slug2', 7, False],
        ['slug3', 6, True],
        ['slug4', 5, False],
        ['slug5', 4, True],
        ['slug6', 3, False],
        ['slug7', 2, True],
        ['slug8', 1, True]
    ]

    @classmethod
    def setUpTestData(cls):
        for td in cls.test_data:
            slug, scoring, is_published = td
            TestDisplayable.objects.create(
                slug=slug,
                scoring=scoring,
                is_published=is_published
            )

    def test_get_url(cls):
        for d in TestDisplayable.objects.all():
            cls.assertEqual(d.url, d.slug + '/')

    def test_get_absolute_url(cls):
        for d in TestDisplayable.objects.all():
            cls.assertEqual(d.get_absolute_url(), 'app_name/' + d.slug + '/')

    def test_public_manager(cls):
        # БД выдаёт то же самое что и вручную отсартированные фикстуры
        cls.assertListEqual(
            [x.slug for x in TestDisplayable.public.all()],
            [x[0] for x in sorted(cls.test_data, key=lambda x: -x[1]) if x[2]]
        )

        # Фикстуры совпадают
        cls.assertEqual(
            TestDisplayable.public.all()[0].slug,
            'slug1'
        )

        # Первый элемент будет с максимальным скорингом
        from django.db.models import Max
        cls.assertEqual(
            TestDisplayable.public.all()[0].scoring,
            TestDisplayable.objects.aggregate(Max('scoring'))['scoring__max']
        )

    def test_field_clean_ok(cls):
        for x in TestDisplayable.objects.all():
            x.clean_fields()

        aditional_test_data = [
            ('slug', ''),
            ('slug1', 'url/'),
            ('slug_1', 'url/url/'),
            ('slug-1-2-lol', 'url/url/url/'),
        ]

        for atd in aditional_test_data:
            x = TestDisplayable(
                slug=atd[0],
                url=atd[1]
            )
            x.clean_fields()

    def test_field_clean_except(cls):
        from django.core.exceptions import ValidationError
        invalid_test_data = [
            ('', ''),
            ('', 'url/'),
            ('slug', '/'),
            ('slug', '/url/'),
            ('slug', '/url//'),
            ('slug', '///'),
            ('slug ', '///'),
            ('slжug', 'url/'),
            ('SLUG', 'url1/url2/'),
            ('SLUG', '///'),
        ]
        for itd in invalid_test_data:
            x = TestDisplayable(
                slug=itd[0],
                url=itd[1]
            )

            cls.assertRaises(ValidationError,
                             x.clean_fields
                             )

    @classmethod
    def tearDownClass(cls):
        # Удаляю всё что создал в тесте
        TestDisplayable.objects.all().delete()
        super(TestingDisplayable, cls).tearDownClass()


class TestingTimeStamped(TestCase):

    """
    TimeStamped
     * Тест работы save() без параметра
     * Тест работы save() с параметром
    """

    def test_save(cls):
        x = TestTimeStamped()
        x.save()
        modified_at_1 = x.modified_at
        x.save()
        modified_at_2 = x.modified_at
        cls.assertNotEqual(modified_at_1, modified_at_2)
        cls.assertLess(modified_at_1, modified_at_2)

    def test_save_auto_now_false(cls):
        x = TestTimeStamped()
        x.save(auto_now=False)
        modified_at_1 = x.modified_at
        x.save(auto_now=False)
        modified_at_2 = x.modified_at
        cls.assertEqual(modified_at_1, modified_at_2)

    @classmethod
    def tearDownClass(cls):
        # Удаляю всё что создал в тесте
        TestTimeStamped.objects.all().delete()
        super(TestingTimeStamped, cls).tearDownClass()


class TestingIndexable(TestCase):

    """
    TimeStamped
     * Тесты проверки соответствия проперти и методов
    """
    test_data = [
        ['title_1', "meta_title_1", "meta_description_1", "meta_keys_1"],
        ['title_2', "meta_title_2", "meta_description_2", "meta_keys_2"],
        ['title_3', "meta_title_3", "meta_description_3", "meta_keys_3"],
        ['title_4', "meta_title_4", "meta_description_4", "meta_keys_4"],
        ['title_5', "meta_title_5", "meta_description_5", "meta_keys_5"],
        ['title_6', "meta_title_6", "meta_description_6", "meta_keys_6"],
        ['title_7', "meta_title_7", "meta_description_7", "meta_keys_7"],
        ['title_8', "meta_title_8", "meta_description_8", "meta_keys_8"]
    ]

    @classmethod
    def setUpTestData(cls):
        for td in cls.test_data:
            title, meta_title, meta_description, meta_keys = td
            TestIndexable.objects.create(
                _title=title,
                _meta_title=meta_title,
                _meta_description=meta_description,
                _meta_keywords=meta_keys,
            )

    def test_title(cls):
        for x in TestIndexable.objects.all():
            cls.assertEqual(x.title, x.get_title())

    def test_meta_title(cls):
        for x in TestIndexable.objects.all():
            cls.assertEqual(x.meta_title, x.get_meta_title())

    def test_meta_description(cls):
        for x in TestIndexable.objects.all():
            cls.assertEqual(x.meta_description, x.get_meta_description())

    def test_meta_keywords(cls):
        for x in TestIndexable.objects.all():
            cls.assertEqual(x.meta_keywords, x.get_meta_keywords())

    @classmethod
    def tearDownClass(cls):
        # Удаляю всё что создал в тесте
        TestIndexable.objects.all().delete()
        super(TestingIndexable, cls).tearDownClass()
