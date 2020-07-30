import re
from typing import List
import nltk

import tensorflow.compat.v1 as tf
import tensorflow_hub as hub

from .models import Sentence


class EmbeddingService(object):

    @classmethod
    def get_sentences(cls, rawtext: str) -> list:
        clear_raw_text = re.sub(r'[\n\t]', '', rawtext)  # TODO more complex clearing
        return nltk.tokenize.sent_tokenize(clear_raw_text)

    @classmethod
    def init_vectorizer(cls):
        g = tf.Graph()
        with g.as_default():
            text_input = tf.placeholder(dtype=tf.string, shape=[None])
            embed = hub.Module('textes/data')
            embedded_text = embed(text_input)
            init_op = tf.group([tf.global_variables_initializer(), tf.tables_initializer()])
        g.finalize()
        session = tf.Session(graph=g)
        session.run(init_op)
        return session, embedded_text, text_input

    @classmethod
    def vectorize_sentences(cls, sentences: List[str] , session, embedded_text, text_input) -> list:
        vectors = session.run(embedded_text, feed_dict={text_input: sentences})
        return [vector.tolist() for vector in vectors]

    @classmethod
    def create_vectors(cls, sentences: List[str]):
        tf_session, embeddings, text_ph = EmbeddingService.init_vectorizer()
        return cls.vectorize_sentences(sentences, tf_session, embeddings, text_ph)

    @classmethod
    def save_vectorized_sentences(cls, sentences: List[str], raw_text_id: int):
        to_save = []
        session, embedded_text, text_input = cls.init_vectorizer()
        vectors = cls.vectorize_sentences(sentences, session, embedded_text, text_input)
        for _index, sentence in enumerate(sentences):
            to_save.append(Sentence(content=sentence, text_id=raw_text_id, vectors=vectors[_index]))
        return Sentence.objects.bulk_create(to_save)

