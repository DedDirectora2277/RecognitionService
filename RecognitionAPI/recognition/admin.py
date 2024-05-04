from django.contrib import admin

from recognition.models import RecognizedText, ImageToRecognize

# Register your models here.
admin.site.register(RecognizedText)
admin.site.register(ImageToRecognize)