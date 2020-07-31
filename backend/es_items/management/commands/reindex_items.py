import logging

from django.core.management import BaseCommand

from es_items.index import SENTENCE_INDEX, SentenceDoc
from es_items.services import EsItemService

from textes.models import Sentence


class Command(BaseCommand):
    _logger = logging.getLogger(f'{__name__}.Command')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._es = EsItemService.init_es_client()

    def handle(self, *args, **options) -> None:
        self._logger.info('Recreating sentence index')
        if self._es.indices.exists(SENTENCE_INDEX):
            self._es.indices.delete(SENTENCE_INDEX)
        SentenceDoc.init()
        self._logger.info('Sentence indexing started')
        EsItemService.add_sentences_to_index(Sentence.objects.all.iterator(), self._es)
        self._logger.info('Sentence indexing finished')
