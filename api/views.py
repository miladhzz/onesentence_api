from django.shortcuts import render
from rest_framework import viewsets
from api.models import Sentence
from api.serializers import SentenceSerializer


class SentenceView(viewsets.ModelViewSet):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer
