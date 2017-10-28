
"""
Модоели для тестирования абстрактных моделей
из core.db.base
"""


from core.db.base import (Describable,
                          Displayable,
                          TimeStamped,
                          Indexable,
                          Named,
                          WebPage
                          )


class TestDescribable(Describable):
    pass


class TestDisplayable(Displayable):

    def get_url(self):
        return self.slug + '/'

    def get_absolute_url(self):
        return "app_name/" + self.url


class TestTimeStamped(TimeStamped):
    pass


class TestIndexable(Indexable):
    pass


class TestNamed(Named):
    pass


class TestWebPage(WebPage):
    def get_url(self):
        return self.slug + '/'

    def get_absolute_url(self):
        return "app_name/" + self.url


class TestDisplayableNotImplemented(Displayable):

    """
    Должнен вызвать NotImplementedError
    так как get_url() не определён.
    """
    pass
