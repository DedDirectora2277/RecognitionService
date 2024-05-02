from django.db import models


# Create your models here.
class RecognizedText(models.Model):
    image_id = models.CharField(max_length=40)
    text = models.TextField(blank=True)

