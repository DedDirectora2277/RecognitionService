from rest_framework import generics
from .models import RecognizedText
from .serializers import RecognizedSerializer
from django.shortcuts import render


# Create your views here.
class RecognitionAPIView(generics.GenericAPIView):
    queryset = RecognizedText.objects.all()
    serializer_class = RecognizedSerializer
