from elasticsearch_dsl import Document, Integer, Keyword, Text, Date, Object, DenseVector
from textes.models import Sentence

SENTENCE_INDEX = 'sentence'


class SentenceDoc(Document):
    id = Integer()
    text_id = Integer()
    content = Text()
    vectors = DenseVector(dims=512)

    class Index:
        name = SENTENCE_INDEX
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
        mappings = {
            "dynamic": "true"
        }
