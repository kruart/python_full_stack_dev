from rest_framework import viewsets
from . import serializers
from . import models


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.filter(is_published=True)
    serializer_class = serializers.PostSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
