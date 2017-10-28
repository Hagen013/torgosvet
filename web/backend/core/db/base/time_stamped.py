from django.db import models
from django.utils import timezone


class TimeStamped(models.Model):

    """
    TimeStamped - изменяемое во времени

    created_at  |
    modified_at | - даты

    Добавлен аргумент auto_now=True на save. Который влияет на
    изменение modified_at в момент сохранения.
    """
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    modified_at = models.DateTimeField(
        verbose_name='Последнее изменение'
    )

    def save(self, auto_now=True, *args, **kwargs):
        if auto_now or self.pk is None:
            self.modified_at = timezone.now()
        super(TimeStamped, self).save(*args, **kwargs)
