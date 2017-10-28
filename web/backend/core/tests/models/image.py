from django.db import models

from core.db.image import Image


class TestImage(Image):
    upload_image_to = 'images/test_image'
    image_key_attribute = 'image_name'

    image_name = models.CharField(
        max_length=128,
        unique=True
    )
