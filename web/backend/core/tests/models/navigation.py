from django.db import models

from core.db.navigation import CategoryPage


class TestCategoryPage(CategoryPage):

    def get_absolute_url(self):
        return 'app_name' + self.get_absolute_url()
