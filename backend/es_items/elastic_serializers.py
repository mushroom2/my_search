from rest_framework_elasticsearch.es_serializer import ElasticModelSerializer

from .index import SentenceDoc
from textes.models import Sentence


class SentenceElasticSerializer(ElasticModelSerializer):
    class Meta:
        model = Sentence
        es_model = SentenceDoc
        fields = (
            'id', 'text_id', 'content', 'vectors'
        )
