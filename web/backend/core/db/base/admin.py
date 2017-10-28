from django.utils.html import format_html


class TimeStampedAdminMixin(object):

    def __init__(self, model, admin_site):
        f = [
            (
                "Даты", {
                    "fields": ("created_at", "modified_at")
                }
            ),
        ]
        if self.fieldsets:
            self.fieldsets += f
        else:
            self.fieldsets = f

        rf = ('created_at', "modified_at")
        if self.readonly_fields:
            self.readonly_fields += rf
        else:
            self.readonly_fields = rf

        super(TimeStampedAdminMixin, self).__init__(model, admin_site)


class DescribableAdminMixin(object):

    def __init__(self, model, admin_site):
        f = [
            (
                "Описание", {
                    "fields": ("description",)
                }
            ),
        ]
        if self.fieldsets:
            self.fieldsets += f
        else:
            self.fieldsets = f

        super(DescribableAdminMixin, self).__init__(model, admin_site)


class DisplayableAdminMinin(object):

    def __init__(self, model, admin_site):
        f = [
            (
                "Веб", {
                    "fields": (
                        ("slug", "scoring"),
                        ("url",),
                        ("show_absolute_url",),
                        ("is_published",),
                    )
                }
            ),
        ]
        if self.fieldsets:
            self.fieldsets += f
        else:
            self.fieldsets = f

        rf = ('url', "show_absolute_url")
        if self.readonly_fields:
            self.readonly_fields += rf
        else:
            self.readonly_fields = rf

        super(DisplayableAdminMinin, self).__init__(model, admin_site)

    def show_absolute_url(self, obj):
        return format_html(
            "<a href='/{url}'>{url}</a>",
            url=obj.get_absolute_url()
        )

    show_absolute_url.short_description = "Full URL"


class IndaxebleAdminMixin(object):

    def __init__(self, model, admin_site):
        f = [
            (
                "СЕО", {
                    "fields": (
                        ("_title", "_meta_title"),
                        ("_meta_description", "_meta_keywords"),
                    )
                }
            ),
        ]
        if self.fieldsets:
            self.fieldsets += f
        else:
            self.fieldsets = f

        super(IndaxebleAdminMixin, self).__init__(model, admin_site)


class WebPageAdminMixin(DisplayableAdminMinin,
                        IndaxebleAdminMixin,
                        TimeStampedAdminMixin,
                        DescribableAdminMixin,
                        ):
    pass
