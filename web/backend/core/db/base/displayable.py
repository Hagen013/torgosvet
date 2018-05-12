from django.db import models
from django.core.validators import RegexValidator


class DisplayableManager(models.Manager):

    def get_queryset(self):
        return super(DisplayableManager, self).get_queryset().\
            filter(is_published=True).\
            order_by('-scoring')


class Displayable(models.Model):

    """
    Displayable - всё то, что может быть отображено на странице.
    требуется определить 2 метода: get_url, get_absolute_url
    slug
    url - обычно совпадает со слагом, но не всегда (CategoryPage)
    get_url - формирование урла (чаще всего просто вернуть слаг)
    get_absolute_url - получение полгоно урла (путь_роутинга+урл)
    scoring - рейтинг, ранжирование
    is_published - опубликована, связзано с DisplayableManager
    slug и url имеют валидаторы
    """
    class Meta:
        abstract = True

    # Castom menager
    objects = models.Manager()
    public = DisplayableManager()

    # Adresses fields
    slug = models.CharField(
        verbose_name="Слаг",
        max_length=1024,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[-_a-z\d]+$',
                message='slug valid error',
            )
        ]
    )

    url = models.CharField(
        verbose_name="URL",
        max_length=2048,
        editable=False,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^(($)|(([-_\da-z]+/)+$))',
                message='slug valid error',
            )
        ]
    )

    def get_url(self):
        msg = "Method get_url() must be implemented by subclass: `{}`"
        raise NotImplementedError(msg.format(self.__class__.__name__))

    def get_absolute_url(self):
        msg = "Method get_absolute_url() must be implemented by subclass: `{}`"
        raise NotImplementedError(msg.format(self.__class__.__name__))

    @property
    def absolute_url(self):
        return self.get_absolute_url()

    scoring = models.IntegerField(
        verbose_name='Скоринг',
        default=0,
    )

    # Bool Fields
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликован'
    )

    def save(self, *args, **kwargs):
        self.url = self.get_url()
        super(Displayable, self).save(*args, **kwargs)
