from django.db import models

from mptt.models import MPTTModel, TreeForeignKey, TreeManager

from ..db import WebPage, Named, Orderable, DisplayableManager


class AbstractCategoryNode(MPTTModel, WebPage, Named, Orderable):

    """
    Конечный класс категории
    """

    class Meta:
        abstract = True
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

