from blog.app.models import Post
from rest_framework import viewsets
from blog.app.serializers import PostSerializer
from blog.app.filters import PostFilter
from django_filters import rest_framework as filters


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_class = PostFilter
