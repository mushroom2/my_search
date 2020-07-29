from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import RawText, Sentence, Vector
from .services import EmbeddingService
from .serializers import RawTextSerizlizer


class RawTextView(ListCreateAPIView):
    queryset = RawText.objects.all()
    serializer_class = RawTextSerizlizer

    def post(self, request, *args, **kwargs):
        raw_text = request.data.get('text')
        new_text = RawText.objects.create(raw_content=raw_text)
        sentences = EmbeddingService.get_sentences(raw_text)
        serializer = self.get_serializer(new_text)
        return Response(serializer.data)
