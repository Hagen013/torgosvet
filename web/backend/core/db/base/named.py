from django.db import models


class Named(models.Model):
    """
    Имеющее имя
    """

    class Meta:
        abstract = True

    name = models.CharField(
        max_length=512,
        verbose_name='Название'
    )
