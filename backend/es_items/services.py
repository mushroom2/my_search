from typing import Iterable

from elasticsearch.helpers import bulk
from elasticsearch_dsl import connections

from django.conf import settings

from textes.models import Sentence
from .elastic_serializers import SentenceElasticSerializer


class EsItemsService(object):
    @classmethod
    def init_es_client(cls):
        return connections.create_connection(
            hosts=settings.ELASTICSEARCH_HOST,
            timeout=settings.ELASTICSEARCH_TIMEOUT
        )

    @classmethod
    def add_sentences_to_index(cls, items: Iterable[Sentence], es_client):
        to_index = (
            SentenceElasticSerializer(sentence).es_instance()
            .to_dict(include_meta=True)
            for sentence in items
        )
        bulk(client=es_client, actions=to_index)
