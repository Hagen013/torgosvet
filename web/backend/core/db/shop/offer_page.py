from django.db import models

from ..base import WebPage, Named
from .offer import Offer, BaseOffer


class OfferPage(BaseOffer,
                WebPage,
                Named
                ):

    class Meta:
        abstract = True
        verbose_name = 'Страница продукта'
        verbose_name_plural = 'Страница продукта'
