from ..base.admin import WebPageAdminMixin
from mptt.admin import MPTTModelAdmin
from mptt.admin import TreeRelatedFieldListFilter

from django.utils.html import format_html


class CategoryPageAdminMixin(WebPageAdminMixin, MPTTModelAdmin):

    def __init__(self, model, admin_site):
        f = [
            (
                "Веб", {
                    "fields": (
                        ("name", "parent",),
                    )
                }
            ),
        ]
        if self.fieldsets:
            self.fieldsets += f
        else:
            self.fieldsets = f

        lf = (
            ('parent', TreeRelatedFieldListFilter),
        )

        if self.list_filter:
            self.list_filter += lf
        else:
            self.list_filter = lf

        super(CategoryPageAdminMixin, self).__init__(model, admin_site)
