from rest_framework.serializers import Serializer
from rest_framework.fields import CharField, DateTimeField, IntegerField, SerializerMethodField
from .models import RawText


class SentecesSerializer(Serializer):
    id = IntegerField()
    content = CharField()


class RawTextBaseSerizlizer(Serializer):
    id = IntegerField()
    created_at = DateTimeField()
    slug = SerializerMethodField()

    def get_slug(self, instance: RawText):
        return instance.raw_content[:42] + '...'


class RawTextDetailSerizlizer(RawTextBaseSerizlizer):
    raw_content = CharField()
    sentences = SerializerMethodField()

    def get_sentences(self, instance: RawText):
        return SentecesSerializer(instance.sentences, many=True).data
