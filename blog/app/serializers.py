from blog.app.models import Post
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Post
            fields = ('id', 'title', 'text')
