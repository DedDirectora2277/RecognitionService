from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Create your models here.


class ImageToRecognize(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    user_id = models.CharField(max_length=40)
    image = models.ImageField(upload_to='temp', default='default_image.jpg')


@receiver(post_delete, sender=ImageToRecognize)
def delete_image(sender, instance, **kwargs):
    # Удаляем файл изображения при удалении объекта ImageModel
    instance.image.delete(False)


class RecognizedText(models.Model):
    user_id = models.CharField(max_length=40)
    image_id = models.CharField(max_length=40)
    text = models.TextField(blank=True)
