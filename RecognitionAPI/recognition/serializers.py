from rest_framework import serializers

from recognition.models import RecognizedText


class RecognizedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecognizedText
        fields = ('image_id', 'recognized_text')
