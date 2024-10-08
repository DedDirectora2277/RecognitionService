from rest_framework import serializers

from recognition.models import RecognizedText, ImageToRecognize


class RecognizedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecognizedText
        fields = ('image_id', 'text')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageToRecognize
        fields = ('id', 'image')
