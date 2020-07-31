from rest_framework.serializers import Serializer
from rest_framework.fields import IntegerField, CharField, SerializerMethodField


class EsItemSerializer(Serializer):
    _score = SerializerMethodField()
    id = IntegerField(source='_source.id')
    text_id = IntegerField(source='_source.text_id')
    content = CharField(source='_source.content')

    def get__score(self, hit):
        return (hit['_score'] - 1) * 100