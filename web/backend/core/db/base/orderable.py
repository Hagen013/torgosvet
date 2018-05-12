from django.db import models


class Orderable(models.Model):
    """
    Orderable - имеющее порядок в последовательности
    order отличается от scoring, назначабщегося автоматически
    """
    class Meta:
        abstract = True

    order = models.IntegerField(
        verbose_name='порядок',
        default=0
    )