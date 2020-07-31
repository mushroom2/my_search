from rest_framework.generics import ListAPIView
from .services import EsItemsService
from .index import SENTENCE_INDEX
from .serializers import EsItemSerializer
from textes.models import Sentence
from rest_framework.response import Response
from rest_framework.request import Request


class EsItemsSearchView(ListAPIView):

    serializer_class = EsItemSerializer
    es_client = EsItemsService.init_es_client()

    def get(self, request: Request, *args, **kwargs) -> Response:
        request_data = request.query_params
        sentence_id = request_data.get('sentence_id')
        sentence = None
        if sentence_id:
            sentence = Sentence.objects.filter(id=sentence_id).first()
        if not sentence:
            return Response({'status': 'error', 'details': 'sentence not found'})
        script_query = {
            "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": "cosineSimilarity(params.query_vector, doc['vectors']) + 1.0",
                    "params": {"query_vector": sentence.vectors}
                }
            }
        }
        response = self.es_client.search(
            index=SENTENCE_INDEX,
            body={
                "query": script_query,
            }
        )
        serializer = self.get_serializer(response['hits']['hits'], many=True)
        return Response(serializer.data)
