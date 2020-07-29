import re
import nltk

import tensorflow.compat.v1 as tf
import tensorflow_hub as hub


class EmbeddingService(object):

    @classmethod
    def get_sentences(cls, rawtext: str) -> list:
        clear_raw_text = re.sub(r'[\n\t]', '', rawtext)  # TODO more complex clearing
        return nltk.tokenize.sent_tokenize(clear_raw_text)

    @classmethod
    def init_vectorizer(cls):
        embed = hub.load('textes/data')
        text_ph = tf.placeholder(tf.string)
        embeddings = embed.signatures['default'](text_ph)
        session = tf.Session()
        session.run(tf.global_variables_initializer())
        session.run(tf.tables_initializer())
        return session, embeddings, text_ph

    @classmethod
    def vectorize_sentence(cls, sentence: str, tf_session: tf.Session, embeddings, text_placeholder) -> list:
        vectors = tf_session.run(embeddings, feed_dict={text_placeholder: sentence})
        a = 10
