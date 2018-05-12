from mptt.models import TreeForeignKey, TreeManager

from core.models import AbstractCategoryNode


class CategoryNode(AbstractCategoryNode):

    """
    Конечный класс категории
    """

    class Meta:
        abstract = False
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        db_index=True,
        related_name='childs'
    )

    def get_url(self):
        return self.url
