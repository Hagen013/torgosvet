import os
import shutil

from django.test import TestCase
from django.conf import settings
from django.core.files import File

from PIL import Image

from .models import TestImage


class TestingImage(TestCase):

    """
    В тесте проверятеся, может ли миксин создаваться,
    нет ли ошибок при создании
    """
    # путь до папки с фикстурами
    images_path = str(settings.MEDIA_ROOT) + '/test_images/'

    @classmethod
    def setUpTestData(cls):
        # ГЕНЕРАЦИЯ ФИКСТУРНЫХ КАРТИНОК
        # (которые не используются в тестах 😡
        # Проверить или создать MEDIA_ROOT
        if not os.path.exists(str(settings.MEDIA_ROOT)):
            os.makedirs(str(settings.MEDIA_ROOT))
        # Удаление перед тестами
        shutil.rmtree(cls.images_path,
                      ignore_errors=True)
        # Создать заного
        os.makedirs(cls.images_path)

        # Создание фикстурных картинок и запись их в бд
        for i in range(0, 255, 5):
            # путь до файла
            file_path = "{path}{name}.jpg".format(name=i,
                                                  path=cls.images_path
                                                  )
            # Создание и сохранение
            Image.new("RGB", (640, 640), (i, i, i)).save(file_path, "JPEG")
            # Добавление пути в список тестовых файлов
            with open(file_path, 'rb') as f:
                TestImage(
                    image_name="image_{i}".format(i=i),
                    image=File(f)
                ).save()

    def test_image_creations(cls):
        # было проверено при формировании фикстур
        # TODO более сложная проверка
        pass

    def test_image_path(cls):
        # было проверено в test_image_rename
        # TODO более сложная проверка
        pass

    def test_image_rename(cls):
        # Создаём файл
        # TODO более сложная проверка
        file_path = "{path}{name}.jpg".format(name='upload_name.jpg',
                                              path=cls.images_path
                                              )
        Image.new("RGB", (640, 640), (123, 3, 7)).save(file_path, "JPEG")
        with open(file_path, 'rb') as f:
            # сохраняем в модель
            x = TestImage(
                image_name="image_new_name",
                image=File(f)
            )
            x.save()

        cls.assertEqual(x.image.name, 'images/test_image/image_new_name.jpg')

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.images_path, ignore_errors=True)
        shutil.rmtree(str(settings.MEDIA_ROOT), ignore_errors=True)
        TestImage.objects.all().delete()
        pass
