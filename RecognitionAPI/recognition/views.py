from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .recognitionFunction import extract_text_from_image
from .models import RecognizedText
from .serializers import RecognizedSerializer, ImageSerializer


# Create your views here.
class RecognitionAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image_instance = serializer.save()

            text = extract_text_from_image(image_instance.image)

            text_instance = RecognizedText.objects.create(image_id=image_instance.id, text=text, user_id=image_instance.
                                                          user_id)

            image_instance.delete()
            text_serializer = RecognizedSerializer(text_instance)
            return Response(text_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
