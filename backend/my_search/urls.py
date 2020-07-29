from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend.textes.views import RawTextView

v1_router = routers.SimpleRouter()
v1_0_patterns = [
    path('raw_text', RawTextView.as_view(), name='raw_text'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1.0/', include((v1_0_patterns, 'my_search'), namespace='v1.0')),
]