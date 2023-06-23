from django.urls import include, path
from rest_framework import routers

from contatos.views import ContatosViewSet

router = routers.DefaultRouter()

router.register(r'contatos', ContatosViewSet)

urlpatterns = [
    path("", include(router.urls)),
]