import re


class EmbeddingService(object):

    @classmethod
    def get_sentences(cls, rawtext: str) -> list:
        clear_raw_text = re.sub(r'[\n\t]', '', rawtext)  # TODO more complex clearing
        return clear_raw_text.split('.')

    @classmethod
    def vectorize_sentence(cls, sentence: str) -> list:
        pass
