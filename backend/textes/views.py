from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import RawText
from .services import EmbeddingService
from .serializers import RawTextSerizlizer
from es_items.services import EsItemsService


class RawTextView(ListCreateAPIView):
    queryset = RawText.objects.all()
    serializer_class = RawTextSerizlizer

    def post(self, request, *args, **kwargs):
        raw_text = request.data.get('raw_text')
        created_text = RawText.objects.create(raw_content=raw_text)
        sentences = EmbeddingService.get_sentences(raw_text)
        sentences_qs = EmbeddingService.save_vectorized_sentences(sentences, created_text.id)
        es_client = EsItemsService.init_es_client()
        EsItemsService.add_sentences_to_index(sentences_qs, es_client)
        serializer = self.get_serializer(created_text)
        return Response(serializer.data)


class RawTextRetrieveView(RetrieveAPIView):
    queryset = RawText.objects.all()
    serializer_class = RawTextSerizlizer
