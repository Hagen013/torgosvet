from django.db import models

from .displayable import Displayable
from .describable import Describable
from .indexable import Indexable
from .time_stamped import TimeStamped


class WebPage(Displayable,
              Describable,
              Indexable,
              TimeStamped,
              ):

    """
    Класс-делигатор.

    Содержит в себе минимальный функционал веб-страницы.

    Необходимо определить методы:
      * get_url()
      * get_absolut_url()

    Поле класса:
      * page_type
    """
    class Meta:
        abstract = True
