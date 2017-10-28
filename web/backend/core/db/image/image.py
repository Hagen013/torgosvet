import os

from django.db import models

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFit


def UploadTo(instance, filename):
    """
    Функция вычисления пути файла
    """
    ext = filename.split('.')[-1]
    path = instance.__class__.upload_image_to + '/'
    full_path = getattr(instance,
                        instance.__class__.image_key_attribute
                        )
    # get filename
    filename = '{full_path}.{ext}'.format(
        full_path=full_path,
        ext=ext
    )
    return os.path.join(path, filename)


class Image(models.Model):

    """
    Image - примесь для объекта с каринкой

    image - Картинка

    upload_image_to - Путь сохранения в папке MEDIA_DIR ('image/goods')
    image_key_attribute - Атрибут в который переименовывается картинка
        может быть проперти в том числе

    По умолчанию image = 'images/no_photo.png'
    upload_image_to должен иметь вид "path/to/dir". (Нет разделителя ни в
    конце ни в начале.)
    """

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super(Image, self).__init__(*args, **kwargs)
        if self.upload_image_to is None or self.image_key_attribute is None:
            msg = """class attributes upload_image_to and image_key_attribute
            must be implemented by subclass: `{}`"""
            raise NotImplementedError(msg.format(self.__class__.__name__))

    upload_image_to = None
    image_key_attribute = None

    thumbnail_width = 246
    thumbnail_height = 328
    thumbnail_upscale = True
    thumbnail_quality = 85

    # Images
    image = models.ImageField(upload_to=UploadTo,
                              default='images/no_photo.png',
                              verbose_name='Картинка',
                              blank=True,
                              )

    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFit(
                                   width=thumbnail_width,
                                   height=thumbnail_height,
                                   upscale=thumbnail_upscale,
                               )],
                               options={'quality': thumbnail_quality})
