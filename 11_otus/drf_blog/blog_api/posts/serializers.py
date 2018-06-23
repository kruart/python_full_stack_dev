from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'
