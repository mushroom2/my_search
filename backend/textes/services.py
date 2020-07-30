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
    def vectorize_sentence(cls, sentence: str, session, embedded_text, text_input) -> list:
        vectors = session.run(embedded_text, feed_dict={text_input: [sentence]})
        return [vector.tolist() for vector in vectors]
