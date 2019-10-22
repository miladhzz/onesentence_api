from django.shortcuts import render
from rest_framework import viewsets
from api.models import Sentence
from api.serializers import SentenceSerializer


class SentenceView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer
