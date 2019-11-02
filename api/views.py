from django.shortcuts import render
from rest_framework import viewsets
from api.models import Sentence
from api.serializers import SentenceSerializer, UserSerializer, GroupSerializer
from django.contrib.auth.models import  User, Group


class SentenceViewSet(viewsets.ModelViewSet):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_jointed')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


