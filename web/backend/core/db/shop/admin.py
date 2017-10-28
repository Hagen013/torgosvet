from ..base import DisplayableAdminMinin, TimeStampedAdminMixin, \
    IndaxebleAdminMixin, DescribableAdminMixin


class OfferAdminMixin(object):

    def __init__(self, model, admin_site):
        f = [
            (
                "Продукт", {
                    "fields": (
                        ("name", "price"),
                        ("model", "vendor"),
                        ("old_price", "is_sale"),
                        ("is_in_stock", "is_new", "is_bestseller",)

                    )
                }
            ),
        ]
        if self.fieldsets:
            self.fieldsets += f
        else:
            self.fieldsets = f

        rf = ('is_sale',)
        if self.readonly_fields:
            self.readonly_fields += rf
        else:
            self.readonly_fields = rf

        super(OfferAdminMixin, self).__init__(model, admin_site)


class OfferPageAdminMixin(DisplayableAdminMinin,
                          OfferAdminMixin,
                          TimeStampedAdminMixin,
                          IndaxebleAdminMixin,
                          DescribableAdminMixin,
                          ):
    pass
