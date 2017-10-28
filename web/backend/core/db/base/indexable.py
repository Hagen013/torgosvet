from django.db import models
from django.forms.models import model_to_dict


class Indexable(models.Model):

    """
    Абстрактный класс Indexable (индексируемая веб страница).

    Логика класса направленна на СЕО.

    page_type - тип страницы(каталог, категория, карточка товара),
    должно быть переопределено в потомках.

    title - заголовок страницы (h1)
    meta_title - мета заголовок
    meta_keywords - ключевые слова
    meta_description - метаописание

    get_title - метод формирования title
    get_meta_title() - метод формирования meta_title
    get_meta_keywords() - метод формирования meta_keywords
    get_meta_description() - метод формирования meta_description

    Последние 4 метода - геттеры для соответствующих полей.
    Переопределить если требуется придать особую логику формирования полей.

    as_indexable() - выводит все поля класса как страницы
    """

    class Meta:
        abstract = True
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    # title
    @property
    def title(self):
        return self.get_title()

    def get_title(self):
        return self._title

    _title = models.CharField(
        blank=True,
        verbose_name='Заголовок',
        max_length=256
    )

    # meta_title
    @property
    def meta_title(self):
        return self.get_meta_title()

    _meta_title = models.CharField(
        blank=True,
        verbose_name='Мета заголовок',
        max_length=256
    )

    def get_meta_title(self):
        return self._meta_title

    # meta_keywords
    @property
    def meta_keywords(self):
        return self.get_meta_keywords()

    _meta_keywords = models.CharField(
        blank=True,
        verbose_name='Мета ключевые слова',
        max_length=256
    )

    def get_meta_keywords(self):
        return self._meta_keywords

    # meta_description
    @property
    def meta_description(self):
        return self.get_meta_description()

    _meta_description = models.CharField(
        blank=True,
        verbose_name='Мета описание',
        max_length=256
    )

    def get_meta_description(self):
        return self._meta_description

    # as_page
    def as_indexable(self):
        """
        Метод возвращает все поля находящиеся в миксине Indexable
        в формате словаря.
        """
        result = model_to_dict(
            self,
            fields=[field.name
                    for field in Indexable._meta.fields]
        )
        result['page_type'] = self.page_type
        return(result)

    def save(self, *args, **kwargs):
        super(Indexable, self).save(*args, **kwargs)
