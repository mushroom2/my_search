from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import RawText, Sentence, Vector
from .services import EmbeddingService
from .serializers import RawTextSerizlizer


class RawTextView(ListCreateAPIView):
    queryset = RawText.objects.all()
    serializer_class = RawTextSerizlizer

    @staticmethod
    def create_sentences(sentences: list, raw_text_id: int):
        to_save = []
        for sentence in sentences:
            to_save.append(Sentence(content=sentence, text_id=raw_text_id))
        return Sentence.objects.bulk_create(to_save)

    @staticmethod
    def create_vectors(sentences: list):
        to_save = []
        tf_session, embeddings, text_ph = EmbeddingService.init_vectorizer()
        for sentence in sentences:
            vectors = EmbeddingService.vectorize_sentence(sentence.content, tf_session, embeddings, text_ph)


    def post(self, request, *args, **kwargs):
        raw_text = request.data.get('raw_text')
        created_text = RawText.objects.create(raw_content=raw_text)
        sentences = EmbeddingService.get_sentences(raw_text)
        created_sentences = self.create_sentences(sentences, created_text.id)
        self.create_vectors(created_sentences)
        serializer = self.get_serializer(created_text)
        return Response(serializer.data)
