from django.db import models


class Describable(models.Model):
    """
    Имеющее описание
    """

    class Meta:
        abstract = True

    description = models.TextField(
        verbose_name="Описание",
        blank=True
    )
