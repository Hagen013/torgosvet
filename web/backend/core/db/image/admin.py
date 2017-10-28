from imagekit.admin import AdminThumbnail


class ImageAdminMixin(object):

    admin_thumbnail = AdminThumbnail(image_field='image')

    def __init__(self, model, admin_site):
        f = [
            (
                "Картинка",
                {
                    'fields': (
                        ('image',),
                    )
                }
            ),
            (
                "Смотреть картинку",
                {
                    'classes': ('collapse',),
                    'fields': ('admin_thumbnail', )
                }
            )
        ]
        if self.fieldsets:
            self.fieldsets += f
        else:
            self.fieldsets = f

        rf = ('admin_thumbnail',)
        if self.readonly_fields:
            self.readonly_fields += rf
        else:
            self.readonly_fields = rf

        super(ImageAdminMixin, self).__init__(model, admin_site)


class ImageAdminInlineMixin(ImageAdminMixin):
    extra = 0
