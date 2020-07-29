from rest_framework.serializers import Serializer
from rest_framework.fields import CharField, DateTimeField, IntegerField


class RawTextSerizlizer(Serializer):
    id = IntegerField()
    raw_content = CharField()
    created_at = DateTimeField()