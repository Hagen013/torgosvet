from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^catalog/$', TemplateView.as_view(template_name="pages/catalog.html")),
    url(r'^product/$', TemplateView.as_view(template_name="pages/product.html")),
    url(r'^components/$', TemplateView.as_view(template_name="pages/components.html"))
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
