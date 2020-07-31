from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from textes.views import RawTextView, RawTextRetrieveView
from es_items.views import EsItemsSearchView

v1_router = routers.SimpleRouter()
v1_0_patterns = [
    path('raw_text', RawTextView.as_view(), name='raw_texts'),
    path('get_similar_sentences', EsItemsSearchView.as_view(), name='get_similar_sentences'),
    re_path(r'raw_text/(?P<pk>\d+)$', RawTextRetrieveView.as_view(), name='raw_text')
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1.0/', include((v1_0_patterns, 'my_search'), namespace='v1.0')),
]