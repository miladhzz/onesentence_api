from rest_framework import serializers
from api.models import Sentence


class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = ('id', 'title', 'create_time')
