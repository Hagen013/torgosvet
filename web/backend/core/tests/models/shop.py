from core.db.shop import (Offer,
                          OfferPage
                          )


class TestOffer(Offer):
    pass


class TestOfferPage(OfferPage):
    def get_url(self):
        return self.slug + '/'

    def get_absolute_url(self):
        return 'app_name' + self.slug + '/'
