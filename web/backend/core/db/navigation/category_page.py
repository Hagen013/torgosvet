from django.db import models
from collections import namedtuple

from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager


from core.db.base import Named, WebPage


class CategoryPage(MPTTModel,
                   WebPage,
                   Named):

    """
    Страница категории - станица иерархического каталога
    """
    class Meta():
        abstract = True

    parent = TreeForeignKey(
        'self',
        verbose_name='Родитель',
        related_name='Потомки',

        null=True,
        blank=True,

        db_index=True
    )

    # Displayable
    def get_url(self):
        """
        2 варианта урла
            * ''                 - пустой, у родителя
            * 'japan/'         |
            * 'japan/g-shock/' | - слаги со слешом в конце
        """
        if self.is_root_node():
            return ""
        else:
            return(self.parent.get_url() +
                   self.slug +
                   "/"
                   )

    def __str__(self):
        return self.name
