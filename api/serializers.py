from rest_framework import serializers
from api.models import Sentence


class SentenceSerializer(serializers.ModelSerializer):
    takhasos = serializers.ReadOnlyField(source='takhasos.title')
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Sentence
        fields = ('id', 'title', 'create_time', 'takhasos', 'user', 'word_count', 'zemanat_price',
                  'mohlat_rooz', 'mohlat_saat')
