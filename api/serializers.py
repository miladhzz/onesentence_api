from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Sentence, Takhasos, SentenceStatus


class SentenceSerializer(serializers.ModelSerializer):
    takhasos = serializers.SlugRelatedField(queryset=Takhasos.objects.all(), slug_field='id')
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    status = serializers.SlugRelatedField(queryset=SentenceStatus.objects.all(), slug_field='id')
    class Meta:
        model = Sentence
        fields = ('id', 'title', 'create_time', 'takhasos', 'user', 'word_count', 'zemanat_price',
                  'mohlat_rooz', 'mohlat_saat', 'status', 'price')
